# PyLCARS

![Tests](https://github.com/StowasserH/pylcars/actions/workflows/tests.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)

Create easily Star Trek influenced LCARS user interfaces with Python and PyQt5.

**PyLCARS** is a Python library for building retro-futuristic user interfaces inspired by the LCARS (Library Computer Access and Retrieval System) from Star Trek. It provides a collection of customizable widgets styled in the iconic 1990s aesthetic, complete with SVG rendering, animation effects, and audio feedback.

## Features

- 🚀 **LCARS-themed Widgets** - Pre-styled UI components matching the classic Star Trek aesthetic
- 🎨 **Customizable Colors** - Built-in LCARS color palette with easy customization
- 🖼️ **SVG Support** - Dynamic vector graphics rendering for crisp scaling
- 🔊 **Audio Integration** - Built-in WAV file playback with PyAudio
- ⚡ **Animation Effects** - Visual feedback effects like "tickle" highlighting
- 📦 **Easy to Use** - Simple API for creating LCARS interfaces
- ✅ **Modern Python** - Full type hints, comprehensive documentation, extensive tests

## Quick Start

### Installation

#### Prerequisites

- Python 3.8 or higher
- PyQt5
- PortAudio libraries (for audio playback)

#### Debian/Ubuntu

```bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-pyqt5 portaudio19-dev
pip install pylcars
```

#### macOS

```bash
brew install python3 portaudio
pip install PyQt5 pylcars
```

#### Windows

1. Install Python 3.8+ from [python.org](https://python.org)
2. Install PyAudio: `pip install pipwin && pipwin install portaudio && pip install pyaudio`
3. Install PyLCARS: `pip install pylcars`

### Basic Example

```python
from PyQt5 import QtWidgets
from pylcars import Lcars, Bracket, Colors

app = QtWidgets.QApplication([])

# Create main window
window = Lcars()
window.setWindowTitle("LCARS Interface")

# Add a button
button = Bracket(window.centralwidget)
button.set_color(Colors.orange)
button.setText("ACTIVATE")
button.setGeometry(100, 100, 200, 50)

window.show()
app.exec_()
```

## Available Widgets

| Widget | Purpose |
|--------|---------|
| **Lcars** | Main window class for LCARS applications |
| **Bracket** | Clickable button with corner bracket styling |
| **Block** | Simple colored rectangle |
| **Deco** | Decorative label with optional SVG |
| **Separator** | Directional divider line |
| **Semicircle** | Rounded bracket in multiple directions |
| **Slider** | Horizontal/vertical slider control |
| **Textline** | Text label with color support |
| **Updown** | Up/down navigation buttons with center button |
| **Menue** | Multi-page menu system with tab navigation |

## Colors

PyLCARS includes an authentic LCARS color palette:

```python
from pylcars import Colors

Colors.orange        # #f90 - Primary LCARS orange
Colors.flieder       # #c9c - Light purple
Colors.blaugrau      # #99c - Blue-gray
Colors.rostbraun     # #c66 - Rust brown
Colors.beige         # #fc9 - Beige
Colors.leuchtblau    # #99f - Bright blue
Colors.apricot       # #f96 - Apricot
Colors.pink          # #c69 - Pink
Colors.hellorange    # #fc4 - Bright orange
Colors.rot           # #c00 - Red
```

## Demo Applications

Two demo applications showcase PyLCARS capabilities:

### Menu Demo
```bash
python -m pylcars.demos.menu
```
Interactive demonstration of widgets, menu system, sliders, and animation effects.

### Sound Demo
```bash
python -m pylcars.demos.sounds
```
Grid of 60 buttons demonstrating audio playback functionality.

## Configuration

PyLCARS uses sensible defaults that can be customized:

```python
from pylcars import Lcars
from pylcars.config import DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT

# All configuration constants are available in pylcars.config module
```

## Development

### Setting Up Development Environment

```bash
# Clone repository
git clone https://github.com/StowasserH/pylcars.git
cd pylcars

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with test dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=pylcars

# Run specific test file
pytest tests/test_imports.py -v
```

### Code Quality

```bash
# Type checking
mypy pylcars/

# Linting
flake8 pylcars/ tests/

# Format code
black pylcars/ tests/
```

## Documentation

- [API Documentation](./docs/) - Detailed class and method documentation
- [Contributing Guide](./CONTRIBUTING.md) - How to contribute to PyLCARS
- [Changelog](./CHANGELOG.md) - Version history and updates

## Project Status

- **Current Version**: 0.1.0
- **Status**: Active Development
- **Python Support**: 3.8, 3.9, 3.10, 3.11, 3.12

## Architecture

PyLCARS is built on:
- **PyQt5** - GUI framework
- **PyAudio** - Audio playback
- **xxhash** - Fast hashing for SVG cache management

### Project Structure

```
pylcars/
├── __init__.py           # Package exports
├── lcars.py              # Main window class
├── colors.py             # LCARS color palette
├── conditions.py         # Status conditions
├── enumeration.py        # Base enumeration class
├── orientation.py        # Direction constants
├── sound.py              # Audio playback
├── config.py             # Configuration constants
├── widgets/              # Widget components
│   ├── widgets.py        # Base widget class
│   ├── bracket.py        # Button widget
│   ├── block.py          # Rectangle widget
│   ├── deco.py           # Decorative label
│   ├── separator.py      # Divider widget
│   ├── slider.py         # Slider control
│   ├── textline.py       # Text label
│   ├── updown.py         # Navigation buttons
│   ├── menue.py          # Menu system
│   ├── semicircle.py     # Rounded bracket
│   └── __init__.py       # Widget exports
└── demos/                # Example applications
    ├── menu.py           # Interactive demo
    └── sounds.py         # Audio demo
```

## Troubleshooting

### Audio playback not working
- Ensure PortAudio is installed: `sudo apt-get install portaudio19-dev` (Debian/Ubuntu)
- Check that your system has working audio output

### PyQt5 import errors
- Reinstall PyQt5: `pip install --upgrade PyQt5`
- On some systems, use system package: `sudo apt-get install python3-pyqt5`

### Display issues
- Some widgets require X11. Use `Xvfb` for headless testing
- Ensure your display supports the required resolution (default 800x480)

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## Authors

- **Harald Stowasser** - *Initial work* - [StowasserH](https://github.com/StowasserH)

See also the list of [contributors](https://github.com/StowasserH/pylcars/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Inspiration

PyLCARS is inspired by the iconic Library Computer Access and Retrieval System (LCARS) interface from Star Trek: The Next Generation and subsequent Star Trek series. The design aesthetic captures the optimistic, functional 1990s sci-fi aesthetic that made Star Trek's user interfaces memorable and instantly recognizable.

## References

- [Star Trek: The Next Generation](https://www.startrek.com/)
- [LCARS Design Philosophy](https://memory-alpha.fandom.com/wiki/LCARS)
- [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)

---

**May your interfaces be bold and your colors be vivid!** 🚀🖖
