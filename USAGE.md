# PyLCARS Usage Guide

Complete documentation for using PyLCARS to create LCARS-themed interfaces.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Basic Window](#basic-window)
3. [Adding Widgets](#adding-widgets)
4. [Colors and Styling](#colors-and-styling)
5. [Advanced Usage](#advanced-usage)
6. [Audio Integration](#audio-integration)
7. [Layouts and Positioning](#layouts-and-positioning)
8. [Common Patterns](#common-patterns)
9. [Troubleshooting](#troubleshooting)

## Getting Started

### Installation

```bash
# Install from PyPI (when available)
pip install pylcars

# Or install from source
git clone https://github.com/StowasserH/pylcars.git
cd pylcars
pip install -e .
```

### Minimal Example

```python
from PyQt5 import QtWidgets
from pylcars import Lcars, Bracket, Colors

# Create application
app = QtWidgets.QApplication([])

# Create main window
window = Lcars()
window.setWindowTitle("My LCARS App")

# Add a button
button = Bracket(window.centralwidget)
button.setText("CLICK ME")
button.set_color(Colors.orange)
button.setGeometry(100, 100, 200, 50)

# Show and run
window.show()
app.exec_()
```

**Output:** A 800x480 window with black background and an orange button

## Basic Window

### Creating the Main Window

```python
from pylcars import Lcars

# Create window with default settings (800x480)
window = Lcars()
window.setWindowTitle("My Application")
window.show()
```

### Customizing Window Size

```python
from PyQt5 import QtCore
from pylcars import Lcars
from pylcars.config import DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT

window = Lcars()
# Change size before showing
window.mainWindowSize = QtCore.QSize(1024, 768)
window.setupUi(window)  # Re-initialize UI
window.show()
```

### Window Properties

```python
# Set properties
window.setWindowTitle("LCARS Interface")
window.setWindowIcon(QtGui.QIcon("icon.png"))

# Full screen
window.showFullScreen()

# Maximized
window.showMaximized()

# Get window size
width = window.width()
height = window.height()
```

### Central Widget

All child widgets should be added to the central widget:

```python
# Access central widget
container = window.centralwidget

# Add children to it
widget = Bracket(window.centralwidget)
widget.setGeometry(10, 10, 100, 40)
```

## Adding Widgets

### Widget Types

PyLCARS provides 10 different widget types:

#### Block - Simple Rectangle

```python
from pylcars import Block, Colors

block = Block(window.centralwidget)
block.set_color(Colors.orange)
block.setGeometry(50, 50, 100, 100)
```

**Use for:** Solid color areas, visual separators, backgrounds

#### Bracket - Button Widget

```python
from pylcars import Bracket

button = Bracket(window.centralwidget)
button.setText("ACTIVATE")
button.set_color(Colors.orange)
button.setGeometry(50, 50, 150, 50)

# Handle clicks
button.clicked.connect(on_button_clicked)

def on_button_clicked():
    print("Button clicked!")
```

**Use for:** Clickable buttons, interactive controls

#### Deco - Decorative Label

```python
from pylcars import Deco, Colors

label = Deco(window.centralwidget)
label.setText("System Status")
label.set_color(Colors.leuchtblau)
label.setGeometry(50, 150, 200, 40)
```

**Use for:** Labels, titles, informational text

#### Textline - Text Label

```python
from pylcars import Textline, Colors

text = Textline(window.centralwidget)
text.setText("Values: 42 / 100")
text.set_color(Colors.beige)
text.setGeometry(50, 200, 300, 30)
```

**Use for:** Status text, values, data display

#### Separator - Divider Line

```python
from pylcars import Separator, Orientation, Colors

# Vertical separator
sep_v = Separator(window.centralwidget)
sep_v.set_color(Colors.flieder)
sep_v.setOrientation(Orientation.right)
sep_v.setGeometry(250, 50, 3, 200)

# Horizontal separator
sep_h = Separator(window.centralwidget)
sep_h.set_color(Colors.flieder)
sep_h.setOrientation(Orientation.bottom)
sep_h.setGeometry(50, 260, 200, 3)
```

**Use for:** Visual dividers, layout separation

#### Slider - Interactive Slider

```python
from pylcars import Slider, Colors

slider = Slider(window.centralwidget)
slider.set_color(Colors.leuchtblau)
slider.setGeometry(50, 300, 400, 40)
slider.setRange(0, 100)
slider.setValue(50)

# Handle value changes
slider.valueChanged.connect(on_slider_changed)

def on_slider_changed(value):
    print(f"Slider value: {value}")
```

**Use for:** Value adjustment, range selection

#### Updown - Navigation Control

```python
from pylcars import Updown, Colors

control = Updown(window.centralwidget)
control.set_color(Colors.orange)
control.setGeometry(50, 350, 80, 80)

# Handle button clicks
control.up_clicked.connect(on_up_clicked)
control.down_clicked.connect(on_down_clicked)

def on_up_clicked():
    print("Up button pressed")

def on_down_clicked():
    print("Down button pressed")
```

**Use for:** Numeric adjustment, list navigation

#### Menue - Multi-Page Menu

```python
from pylcars import Menue, Colors

menu = Menue(window.centralwidget)
menu.set_color(Colors.orange)

# Add pages
menu.add_page({
    'title': 'Main',
    'items': [
        {'name': 'Option 1', 'callback': on_option1},
        {'name': 'Option 2', 'callback': on_option2},
    ]
})

menu.add_page({
    'title': 'Settings',
    'items': [
        {'name': 'Audio', 'callback': on_audio},
        {'name': 'Display', 'callback': on_display},
    ]
})

menu.setGeometry(50, 50, 700, 400)
```

**Use for:** Menu systems, navigation, multi-page interfaces

#### Semicircle - Rounded Bracket

```python
from pylcars import Semicircle, Orientation, Colors

corner = Semicircle(window.centralwidget)
corner.set_color(Colors.apricot)
corner.setOrientation(Orientation.left)
corner.setGeometry(50, 50, 50, 50)
```

**Use for:** Corner decorations, visual flourishes

### Widget Common Methods

All widgets support these methods:

```python
# Positioning and sizing
widget.setGeometry(x, y, width, height)
widget.setPos(x, y)
widget.setSize(width, height)

# Visibility
widget.show()
widget.hide()
widget.setVisible(True)

# Styling
widget.set_color("#f90")              # Set color (hex string)
widget.set_color(Colors.orange)       # Or use constant
widget.setFont(font)                  # Set font

# Text (if applicable)
widget.setText("Text")
widget.text()                         # Get text

# Visual effects
widget.tickle(Colors.orange)          # Flash for 300ms
widget.tockle(Colors.blue)            # Toggle color

# Parent/child
widget.setParent(parent)
widget.parent()
```

## Colors and Styling

### Using LCARS Colors

```python
from pylcars import Colors

# Access colors by name
Colors.orange        # '#f90'
Colors.flieder       # '#c9c'
Colors.blaugrau      # '#99c'
Colors.rostbraun     # '#c66'
Colors.beige         # '#fc9'
Colors.leuchtblau    # '#99f'
Colors.apricot       # '#f96'
Colors.pink          # '#c69'
Colors.hellorange    # '#fc4'
Colors.rot           # '#c00'
```

### Custom Colors

```python
from pylcars import Block

# Use any hex color
widget = Block(window.centralwidget)
widget.set_color("#00ff00")     # Lime green
widget.set_color("#ff00ff")     # Magenta
widget.set_color("#0000ff")     # Blue
```

### Color Themes

Create a custom color scheme:

```python
class CustomColors:
    """Custom LCARS color theme."""
    primary = "#00ff00"      # Lime
    secondary = "#00aa00"    # Dark green
    accent = "#ffff00"       # Yellow
    warning = "#ff0000"      # Red
    text = "#ffffff"         # White
    background = "#000000"   # Black

# Use in application
button = Bracket(window.centralwidget)
button.set_color(CustomColors.primary)
```

### Text Styling

```python
from PyQt5 import QtGui
from pylcars import Textline

# Create custom font
font = QtGui.QFont()
font.setFamily("LCARS")
font.setPointSize(24)
font.setBold(True)

# Apply to widget
text = Textline(window.centralwidget)
text.setFont(font)
text.setText("BOLD TEXT")
```

## Advanced Usage

### Event Handling

```python
from PyQt5 import QtCore

# Connect button clicks
button = Bracket(window.centralwidget)
button.clicked.connect(on_button_clicked)

# Connect slider changes
slider = Slider(window.centralwidget)
slider.valueChanged.connect(on_value_changed)
slider.sliderMoved.connect(on_slider_moved)

# Custom slots
def on_button_clicked():
    print("Button clicked!")
    widget.tickle(Colors.orange)  # Flash effect

def on_value_changed(value):
    print(f"New value: {value}")
```

### State Management

```python
# Store state in instance variables
class MyApp:
    def __init__(self):
        self.window = Lcars()
        self.state = {
            'mode': 'standby',
            'power': 100,
            'temperature': 42,
        }
        self.setup_ui()

    def setup_ui(self):
        # Create widgets with callbacks
        button = Bracket(self.window.centralwidget)
        button.clicked.connect(self.on_mode_button)

    def on_mode_button(self):
        if self.state['mode'] == 'standby':
            self.state['mode'] = 'active'
        else:
            self.state['mode'] = 'standby'
        self.update_display()

    def update_display(self):
        # Update UI based on state
        status = Textline(self.window.centralwidget)
        status.setText(f"Mode: {self.state['mode']}")
```

### Custom Widget Creation

```python
from pylcars import Widgets
from PyQt5 import QtWidgets

class CustomControl(Widgets, QtWidgets.QWidget):
    """Custom LCARS widget."""

    def __init__(self, lcars, parent=None):
        Widgets.__init__(self, lcars)
        QtWidgets.QWidget.__init__(self, parent)
        self.setup_ui()

    def setup_ui(self):
        # Add child widgets
        button = Bracket(self)
        button.setGeometry(0, 0, 100, 40)

    def set_value(self, value):
        """Custom method."""
        self.value = value
        self.update()
```

### Timer-Based Updates

```python
from PyQt5 import QtCore
import time

class AnimatedApp:
    def __init__(self):
        self.window = Lcars()
        self.counter = 0

        # Setup timer for updates
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(100)  # Every 100ms

        self.window.show()

    def update(self):
        """Called periodically."""
        self.counter += 1

        # Update UI
        if self.counter % 10 == 0:
            # Flash effect every second
            widget.tickle(Colors.orange)
```

## Audio Integration

### Playing Sounds

```python
from pylcars import Lcars

window = Lcars()

# Enable audio
window.set_play_sound(True)

# Set and play a sound file
window.set_sound_file("path/to/sound.wav")
window.play_sound()
```

### Integration with UI Events

```python
from pylcars import Bracket, Lcars

window = Lcars()
window.set_play_sound(True)
window.set_sound_file("click.wav")

button = Bracket(window.centralwidget)
button.clicked.connect(lambda: window.play_sound())
button.setGeometry(50, 50, 150, 50)
button.setText("BEEP")
```

### Sound File Requirements

- **Format:** WAV (RIFF/PCM)
- **Sample rates:** 8000Hz, 16000Hz, 44100Hz, 48000Hz
- **Bit depth:** 8-bit, 16-bit, 24-bit, 32-bit
- **Channels:** Mono, Stereo

### Managing Multiple Sounds

```python
class SoundManager:
    def __init__(self, window):
        self.window = window
        self.sounds = {
            'click': 'sounds/click.wav',
            'alert': 'sounds/alert.wav',
            'success': 'sounds/success.wav',
        }

    def play(self, sound_name):
        if sound_name in self.sounds:
            path = self.sounds[sound_name]
            self.window.set_sound_file(path)
            self.window.play_sound()

# Usage
manager = SoundManager(window)
manager.play('click')
manager.play('alert')
```

## Layouts and Positioning

### Absolute Positioning

```python
# Position widgets by coordinates
widget.setGeometry(x, y, width, height)

button1 = Bracket(window.centralwidget)
button1.setGeometry(50, 50, 100, 40)    # x=50, y=50, w=100, h=40

button2 = Bracket(window.centralwidget)
button2.setGeometry(200, 50, 100, 40)   # Next to button1
```

### Grid Layout

```python
# Create a grid of identical items
cols = 6
rows = 10
button_width = 120
button_height = 40
spacing = 10

for row in range(rows):
    for col in range(cols):
        x = col * (button_width + spacing)
        y = row * (button_height + spacing)

        button = Bracket(window.centralwidget)
        button.setText(f"{row*cols + col + 1}")
        button.setGeometry(x, y, button_width, button_height)
```

### Vertical Stack

```python
# Stack widgets vertically
y_offset = 50
widget_height = 50
spacing = 10

for i in range(5):
    widget = Block(window.centralwidget)
    y = y_offset + i * (widget_height + spacing)
    widget.setGeometry(50, y, 200, widget_height)
    widget.set_color(Colors.colors[i])
```

### Responsive Sizing

```python
# Adapt to window size
def on_window_resized():
    window_width = window.width()
    window_height = window.height()

    # Position widget relative to window
    margin = 20
    widget_width = window_width - 2 * margin
    widget_height = window_height - 2 * margin

    main_widget.setGeometry(margin, margin, widget_width, widget_height)

# Connect resize event
window.resizeEvent = lambda event: on_window_resized()
```

## Common Patterns

### Status Display

```python
from pylcars import Textline, Colors

class StatusDisplay:
    def __init__(self, parent):
        self.status = Textline(parent)
        self.status.set_color(Colors.leuchtblau)
        self.status.setGeometry(50, 50, 300, 30)

    def set_status(self, text):
        self.status.setText(text)

    def set_warning(self):
        self.status.set_color(Colors.rot)

    def set_normal(self):
        self.status.set_color(Colors.leuchtblau)

# Usage
display = StatusDisplay(window.centralwidget)
display.set_status("System Ready")
display.set_warning()
display.set_status("Warning: Low Power")
```

### Toggle Button

```python
from pylcars import Bracket, Colors

class ToggleButton:
    def __init__(self, parent, on_color, off_color):
        self.button = Bracket(parent)
        self.on_color = on_color
        self.off_color = off_color
        self.is_on = False

        self.button.clicked.connect(self.toggle)

    def toggle(self):
        self.is_on = not self.is_on
        color = self.on_color if self.is_on else self.off_color
        self.button.set_color(color)
        self.button.tickle(color)

# Usage
toggle = ToggleButton(
    window.centralwidget,
    on_color=Colors.orange,
    off_color=Colors.blaugrau
)
toggle.button.setGeometry(100, 100, 100, 40)
```

### Value Slider with Display

```python
from pylcars import Slider, Textline, Colors

class ValueDisplay:
    def __init__(self, parent, label, min_val, max_val):
        self.slider = Slider(parent)
        self.slider.setRange(min_val, max_val)
        self.slider.set_color(Colors.orange)

        self.display = Textline(parent)
        self.display.set_color(Colors.beige)

        self.slider.valueChanged.connect(self.on_value_changed)

    def on_value_changed(self, value):
        self.display.setText(f"Value: {value}")

# Usage
power = ValueDisplay(window.centralwidget, "Power", 0, 100)
power.slider.setGeometry(50, 100, 400, 40)
power.display.setGeometry(50, 150, 200, 30)
```

### Modal Dialog

```python
from PyQt5 import QtWidgets
from pylcars import Bracket, Colors

def show_confirmation(title, message):
    dialog = QtWidgets.QDialog()
    dialog.setWindowTitle(title)
    dialog.resize(300, 150)

    # Message
    label = QtWidgets.QLabel(message, dialog)
    label.move(20, 20)

    # Yes button
    yes_btn = QtWidgets.QPushButton("YES", dialog)
    yes_btn.clicked.connect(dialog.accept)
    yes_btn.move(50, 100)

    # No button
    no_btn = QtWidgets.QPushButton("NO", dialog)
    no_btn.clicked.connect(dialog.reject)
    no_btn.move(150, 100)

    return dialog.exec_() == QtWidgets.QDialog.Accepted

# Usage
if show_confirmation("Confirm", "Proceed?"):
    print("User said yes")
```

## Troubleshooting

### Common Issues

#### "No module named 'pylcars'"

```bash
# Install package
pip install -e .

# Or add to Python path
import sys
sys.path.insert(0, '/path/to/pylcars')
```

#### Audio doesn't work

```bash
# Install PortAudio (required for PyAudio)
# Ubuntu/Debian
sudo apt-get install portaudio19-dev

# macOS
brew install portaudio

# Verify PyAudio installation
python -c "import pyaudio; print(pyaudio.__version__)"
```

#### Window doesn't display

```python
# Ensure you call show()
window.show()

# Run the event loop
app.exec_()

# Without this, window closes immediately
```

#### Widgets don't appear

```python
# Widgets need explicit geometry
widget = Bracket(window.centralwidget)
widget.setGeometry(50, 50, 100, 40)  # Required!

# Without geometry, widget has 0 size
```

#### Memory issues with audio

```python
# Disable audio if not needed
window.set_play_sound(False)

# Or manage streams explicitly
for stream in window.streams:
    stream.stop_stream()
    stream.close()
window.streams.clear()
```

### Performance Tips

1. **Cache SVG renders** - Reusing colors avoids re-rendering
2. **Limit widget count** - Large UIs with 100+ widgets may slow down
3. **Use simple colors** - Hex colors don't require SVG rendering
4. **Batch updates** - Update multiple widgets together
5. **Disable audio** - If not using sound, disable via `set_play_sound(False)`

### Debugging

```python
import logging

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

# Check widget properties
print(f"Position: {widget.pos()}")
print(f"Size: {widget.size()}")
print(f"Color: {widget.color}")

# Verify parent relationships
print(f"Parent: {widget.parent()}")
print(f"Children: {widget.children()}")
```

## Complete Example Application

```python
"""Complete LCARS application example."""

from PyQt5 import QtWidgets, QtCore
from pylcars import (
    Lcars, Bracket, Block, Textline, Slider,
    Updown, Separator, Colors, Orientation
)

class LCARSApp:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.window = Lcars()
        self.window.setWindowTitle("LCARS System")
        self.setup_ui()

    def setup_ui(self):
        """Build user interface."""
        central = self.window.centralwidget

        # Title
        title = Textline(central)
        title.setText("LCARS CONTROL SYSTEM")
        title.set_color(Colors.leuchtblau)
        title.setGeometry(50, 20, 700, 40)

        # Power control
        power_label = Textline(central)
        power_label.setText("Power Level:")
        power_label.set_color(Colors.beige)
        power_label.setGeometry(50, 80, 150, 30)

        self.power_slider = Slider(central)
        self.power_slider.set_color(Colors.orange)
        self.power_slider.setRange(0, 100)
        self.power_slider.setGeometry(220, 80, 300, 40)
        self.power_slider.valueChanged.connect(self.on_power_changed)

        # Power value display
        self.power_value = Textline(central)
        self.power_value.set_color(Colors.hellorange)
        self.power_value.setGeometry(530, 80, 100, 30)

        # Vertical separator
        sep = Separator(central)
        sep.set_color(Colors.flieder)
        sep.setGeometry(50, 130, 3, 300)

        # Control buttons
        buttons = [
            ("ACTIVATE", 80, Colors.orange),
            ("STANDBY", 135, Colors.blaugrau),
            ("RESET", 190, Colors.rot),
        ]

        for text, y, color in buttons:
            btn = Bracket(central)
            btn.setText(text)
            btn.set_color(color)
            btn.setGeometry(80, y, 150, 40)
            btn.clicked.connect(lambda t=text: self.on_button(t))

        # Status display
        self.status = Textline(central)
        self.status.setText("Status: Online")
        self.status.set_color(Colors.leuchtblau)
        self.status.setGeometry(80, 270, 400, 30)

    def on_power_changed(self, value):
        """Handle power slider changes."""
        self.power_value.setText(f"{value}%")
        if value < 20:
            self.power_value.set_color(Colors.rot)
        elif value < 50:
            self.power_value.set_color(Colors.hellorange)
        else:
            self.power_value.set_color(Colors.orange)

    def on_button(self, button_text):
        """Handle button clicks."""
        self.status.setText(f"Status: {button_text}")
        self.window.centralwidget.findChildren(Textline)[0].tickle(Colors.orange)

    def run(self):
        """Start the application."""
        self.window.show()
        self.app.exec_()

if __name__ == "__main__":
    app = LCARSApp()
    app.run()
```

---

For more examples, see the `pylcars/demos/` directory.
