# PyLCARS Architecture

This document describes the architecture, design decisions, and internal structure of PyLCARS.

## Overview

PyLCARS is built on a layered architecture with clear separation of concerns:

```
┌─────────────────────────────────────────────────────────────┐
│                    Application Layer                         │
│             (Demo Apps, User Applications)                   │
└─────────────────────────────────────────────────────────────┘
                            ▲
┌─────────────────────────────────────────────────────────────┐
│                    Widget Layer                              │
│  (Bracket, Block, Slider, Menue, Textline, Updown, etc.)   │
└─────────────────────────────────────────────────────────────┘
                            ▲
┌─────────────────────────────────────────────────────────────┐
│                    Core Layer                                │
│    (Lcars, Sound, Colors, Conditions, Orientation)          │
└─────────────────────────────────────────────────────────────┘
                            ▲
┌─────────────────────────────────────────────────────────────┐
│               External Dependencies                          │
│         (PyQt5, PyAudio, xxhash, wave)                       │
└─────────────────────────────────────────────────────────────┘
```

## Core Components

### 1. **Main Window (lcars.py)**

The `Lcars` class is the foundation of every PyLCARS application.

```python
class Lcars(Sound, QtWidgets.QMainWindow):
    """Main window combining QMainWindow + Sound functionality."""
```

**Key Features:**
- Inherits from both `Sound` and `QtWidgets.QMainWindow` (multiple inheritance)
- Provides default black background and LCARS styling
- Default window size: 800x480 pixels (configurable via `config.py`)
- Central widget for placing child widgets

**Responsibilities:**
- Window initialization and setup
- UI composition (centralwidget)
- Signal-slot connection setup
- Integration with audio playback

### 2. **Audio System (sound.py)**

The `Sound` class manages WAV file playback using PyAudio.

```python
class Sound:
    """Audio playback manager with multi-stream support."""
```

**Key Features:**
- Manages multiple concurrent audio streams
- Proper resource cleanup (fixed in 0.1.0)
- Callback-based asynchronous playback
- Error handling for file operations

**Design Decisions:**
- Uses PyAudio for cross-platform audio support
- Streams kept in list for lifecycle management
- Wave files kept open during playback (callback closure)
- Graceful error handling with logging

**Resource Management:**
- Streams cleanup in `__del__` for garbage collection
- Proper termination of PyAudio instance
- List comprehension for safe stream filtering

### 3. **Widget System (widgets/)**

#### **Base Widget Class (widgets.py)**

```python
class Widgets:
    """Base class with SVG rendering, styling, and effects."""
```

**Core Functionality:**
- SVG template rendering with dynamic color substitution
- SVG caching for performance (using xxhash)
- Font management (default: "LCARS" font, 26pt)
- Visual feedback effects (tickle, tockle)
- Stylesheet composition

**Key Methods:**
- `adapt_svg(color)` - Renders SVG with specific color
- `set_default_font(fontname, size)` - Configure widget fonts
- `tickle(color)` - Flash widget for 300ms
- `tockle(color)` - Toggle widget color
- `paint_back(color)` - Apply color via stylesheet

#### **Widget Hierarchy**

All widgets inherit from `Widgets` and a PyQt5 base class:

```
Widgets (Base)
├── Block (QFrame)           - Solid rectangle
├── Bracket (QPushButton)    - Clickable button
├── Deco (QLabel)           - Decorative text
├── Separator (QFrame)      - Directional line
├── Slider (QSlider)        - Interactive slider
├── Textline (QLabel)       - Text label
├── Updown (QWidget)        - Navigation control
├── Menue (QWidget)         - Multi-page menu
└── Semicircle (QWidget)    - Rounded bracket
```

**Widget Design Pattern:**
- Composition: Widgets wrap PyQt5 components
- Styling: Custom stylesheets + SVG rendering
- Colors: Use LCARS color scheme or custom hex values
- Signals: Standard PyQt5 signals available

### 4. **Enumerations (colors.py, conditions.py, orientation.py)**

#### **Colors**
```python
class Colors(Enumeration):
    orange = '#f90'
    flieder = '#c9c'
    blaugrau = '#99c'
    # ... etc
```
Provides LCARS color constants as static attributes.

#### **Conditions**
```python
class Conditions(Enumeration):
    alert = 'alert'
    info = 'info'
    use = 'use'
    active = 'active'
```
Status indicators mapped to colors for semantic meaning.

#### **Orientation**
```python
class Orientation(Enumeration):
    left = 0
    right = 1
    top = 2
    bottom = 3
```
Direction constants for widgets like `Separator` and `Semicircle`.

#### **Base Enumeration**
```python
class Enumeration:
    """Pattern for immutable attribute sets."""
```
Provides safe, immutable enumeration pattern without Python's `Enum` module dependency.

### 5. **Configuration (config.py)**

Centralized constants for easy tuning:

```python
DEFAULT_WINDOW_WIDTH = 800
DEFAULT_WINDOW_HEIGHT = 480
TICKLE_DURATION_MS = 300
AUDIO_CHUNK_SIZE = 256
# ... more constants
```

**Benefits:**
- Single source of truth for magic numbers
- Easy theme/sizing customization
- No scattered hardcoded values
- Type hints for all constants

## Design Patterns

### 1. **Multiple Inheritance**

```python
class Lcars(Sound, QtWidgets.QMainWindow):
    pass
```

**Reasoning:**
- Combines audio capability with window functionality
- Clean API: `lcars_window.play_sound()` works naturally
- Python's MRO (Method Resolution Order) handles conflicts

**Risk Mitigation:**
- Explicit `__init__` calls to both parent classes
- Type hints clarify inheritance
- Documentation explains interaction

### 2. **Mixin Pattern**

The `Widgets` mixin provides common functionality:
- SVG rendering
- Styling and theming
- Font management
- Visual effects

```python
class Block(Widgets, QtWidgets.QFrame):
    def __init__(self, lcars, svg=None):
        Widgets.__init__(self, lcars, svg)
        QtWidgets.QFrame.__init__(self, lcars)
```

### 3. **Callback-Based Audio**

PyAudio uses callbacks for streaming:

```python
def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return data, pyaudio.paContinue
```

**Design Decision:**
- Asynchronous playback (doesn't block UI)
- Multiple streams can play simultaneously
- Closure captures wave file reference

### 4. **SVG Caching**

Performance optimization for SVG rendering:

```python
# Hash SVG + color to create cache key
hash = xxhash.xxh32(svg_content + color).hexdigest()
cache_file = f"background/{hash}.svg"

if os.path.exists(cache_file):
    use_cached_svg()
else:
    render_and_cache_svg()
```

## Data Flow

### Window Creation Flow

```
QApplication
    ↓
Lcars.__init__()
    ├─ Sound.__init__()           # Initialize audio
    ├─ QMainWindow.__init__()     # Initialize window
    ├─ setupUi()                  # Setup window properties
    ├─ retranslateUi()            # Set titles/text
    └─ setGeometry()              # Set window size
```

### Widget Creation Flow

```
Widget Class (e.g., Bracket)
    ├─ __init__()
    │   ├─ Widgets.__init__()     # Initialize styling/SVG
    │   └─ PyQt5Class.__init__()  # Initialize Qt component
    ├─ set_color(color)           # Apply color
    │   └─ adapt_svg(color)       # Render/cache SVG
    │       └─ paint_back(color)  # Apply stylesheet
    └─ setText()/setGeometry()    # Configure appearance
```

### Audio Playback Flow

```
play_sound() / set_sound_file()
    ↓
sound(file_path)
    ├─ Clean inactive streams
    ├─ wave.open(file)
    ├─ Define callback function
    ├─ PyAudio.open(stream)
    │   └─ Callback called repeatedly
    │       └─ wf.readframes()
    │           └─ Stream continues until EOF
    └─ Append stream to list
```

## Threading Model

**Single-threaded PyQt5 event loop:**
- All UI operations happen on main thread
- Audio callback runs in PyAudio thread (safe)
- Callback only reads from wave file (no UI updates)
- No race conditions because UI stays on main thread

## Type System

**Full type hints throughout:**

```python
def set_color(self, color: str) -> None:
    """Set widget color.

    Args:
        color: Hex color string (e.g., '#f90', '#0f0').
    """
```

**Benefits:**
- IDE autocomplete support
- Static type checking with mypy
- Self-documenting code
- Catch errors at development time

## Error Handling

**Strategy: Fail gracefully**

1. **File Operations**
   ```python
   try:
       wf = wave.open(file, 'rb')
   except (FileNotFoundError, wave.Error) as e:
       print(f"Error: {e}")
       return
   ```

2. **Resource Cleanup**
   ```python
   try:
       if stream.is_active():
           stream.stop_stream()
   except Exception:
       pass  # Already closed or invalid
   ```

3. **Destructor Safety**
   ```python
   def __del__(self):
       try:
           # Cleanup code
       except Exception:
           pass  # Suppress errors during shutdown
   ```

## Performance Considerations

### SVG Caching
- Expensive SVG rendering cached by xxhash
- Huge performance boost for frequently-used colors
- Cache folder: `./background/`

### Audio Streaming
- 256-byte chunks reduce latency
- Callback-based prevents blocking
- Multiple streams handled efficiently

### Memory Management
- Proper cleanup in `__del__` prevents leaks
- Stream list maintained for lifecycle
- Wave files closed after playback

## Testing Architecture

**Test Pyramid:**

```
        /\
       /E2E\          (Demo apps work)
      /─────\
     /Unit  \         (Component tests)
    /─────────\
   /Integration\      (Module imports)
  /─────────────\
```

**Test Coverage:**
- Imports: Verify all modules load
- Enumerations: Validate color/condition values
- Type hints: mypy validation
- Integration: Demo apps as smoke tests

## Extension Points

### Adding New Widgets

1. Inherit from `Widgets` and PyQt5 base
2. Call `Widgets.__init__(lcars, svg)` in `__init__`
3. Implement widget-specific behavior
4. Use `set_color()` for LCARS styling

### Adding New Colors

```python
# In colors.py
class Colors(Enumeration):
    new_color = '#abc'  # Add here
```

### Customizing Configuration

```python
# In config.py
CUSTOM_SETTING = 42  # Add here
```

Then import and use:
```python
from pylcars.config import CUSTOM_SETTING
```

## Dependencies Analysis

### PyQt5 (GUI Framework)
- Core dependency for all UI
- Handles window, widgets, events, signals
- Cross-platform support (Windows, macOS, Linux)

### PyAudio (Audio I/O)
- Provides audio stream access via PortAudio
- Required for sound playback
- Optional in future versions

### xxhash (Fast Hashing)
- Used only for SVG cache key generation
- Fast hashing for performance
- Could be replaced with hashlib if needed

### wave (Standard Library)
- Read WAV file metadata
- Frame data reading
- Built-in, no external dependency

## Future Architecture Improvements

1. **Plugin System** - Allow custom widget registration
2. **Theme Engine** - Separate theme files from code
3. **Animation Framework** - More sophisticated effects
4. **Scene Graph** - Hierarchical widget composition
5. **Async/Await** - Modern async patterns for audio
6. **Reactive Programming** - RxPy for event streams

## Summary

PyLCARS provides:
- ✅ Clean separation of concerns (core, widgets, apps)
- ✅ Type-safe codebase with hints
- ✅ Well-documented architecture
- ✅ Extensible widget system
- ✅ Proper resource management
- ✅ Cross-platform compatibility
- ✅ Test coverage foundation

The architecture prioritizes **simplicity**, **maintainability**, and **extensibility** while staying true to the retro LCARS aesthetic.
