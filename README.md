# PyLCARS

![Tests](https://github.com/StowasserH/pylcars/actions/workflows/tests.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Version 0.1.0](https://img.shields.io/badge/Version-0.1.0-green.svg)

> Create Star Trek LCARS-inspired user interfaces with Python and PyQt5.

**PyLCARS** is a Python library that brings the iconic LCARS (Library Computer Access and Retrieval System) aesthetic from Star Trek to modern applications. Build retro-futuristic UIs with pre-styled widgets, smooth animations, SVG rendering, and integrated audio feedback.

## 🚀 Quick Start

```python
from PyQt5 import QtWidgets
from pylcars import Lcars, Bracket, Colors

app = QtWidgets.QApplication([])
window = Lcars()

button = Bracket(window.centralwidget)
button.setText("ENGAGE")
button.set_color(Colors.orange)
button.setGeometry(300, 200, 200, 50)

window.show()
app.exec_()
```

## ✨ Features

- **🎨 LCARS-themed Widgets** - Pre-styled UI components matching the Star Trek aesthetic
- **🖼️ SVG Support** - Dynamic vector graphics with automatic caching
- **🔊 Audio Integration** - Built-in WAV file playback with PyAudio
- **⚡ Animation Effects** - Visual feedback including "tickle" highlighting
- **🎯 Type-Safe** - Full type hints for IDE support and static analysis
- **📚 Well-Documented** - Comprehensive docstrings and usage guides
- **✅ Tested** - Pytest suite with GitHub Actions CI/CD
- **🔧 Customizable** - Easy theming and configuration
- **📦 Modern Python** - Pure Python 3.8+ with minimal dependencies

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- PyQt5
- PortAudio (for audio support)

### Ubuntu/Debian

```bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-pyqt5 portaudio19-dev

pip install pylcars
```

### macOS

```bash
brew install python3 portaudio
pip install PyQt5 pylcars
```

### Windows

1. Install Python 3.8+ from [python.org](https://www.python.org)
2. Install PyAudio and PyQt5:
   ```bash
   pip install PyQt5 pylcars
   ```
   For audio support, use `pipwin`:
   ```bash
   pip install pipwin
   pipwin install portaudio
   pip install pyaudio
   ```

### From Source

```bash
git clone https://github.com/StowasserH/pylcars.git
cd pylcars
pip install -e .
```

## 📖 Documentation

- **[Usage Guide](USAGE.md)** - Complete usage documentation with examples
- **[Architecture](ARCHITECTURE.md)** - System design and internal structure
- **[Contributing](CONTRIBUTING.md)** - Development guidelines
- **[Changelog](CHANGELOG.md)** - Version history and updates

## 🎮 Demo Applications

Try the included examples:

```bash
# Interactive widget showcase
python -m pylcars.demos.menu

# Color palette display
python -m pylcars.demos.colors_showcase

# All widgets in one place
python -m pylcars.demos.widgets_showcase

# Custom theme example
python -m pylcars.demos.custom_theme

# Minimal "Hello LCARS" window
python -m pylcars.demos.simple_window

# Audio playback grid
python -m pylcars.demos.sounds
```

## 🧩 Available Widgets

| Widget | Purpose | Example |
|--------|---------|---------|
| **Bracket** | Clickable button with corner styling | `Bracket(window.centralwidget).setText("CLICK")` |
| **Block** | Simple colored rectangle | `Block(window.centralwidget).set_color(Colors.orange)` |
| **Deco** | Decorative label with SVG | `Deco(window.centralwidget).setText("Title")` |
| **Separator** | Directional divider line | `Separator(window.centralwidget).setOrientation(Orientation.right)` |
| **Slider** | Interactive value slider | `Slider(window.centralwidget).setRange(0, 100)` |
| **Textline** | Text label with color | `Textline(window.centralwidget).setText("Status")` |
| **Updown** | Navigation buttons with center | `Updown(window.centralwidget).setGeometry(...)` |
| **Menue** | Multi-page menu system | `Menue(window.centralwidget).add_page(...)` |
| **Semicircle** | Rounded corner decoration | `Semicircle(window.centralwidget).setOrientation(...)` |
| **Lcars** | Main window class | `window = Lcars()` |

## 🎨 LCARS Color Palette

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

Or use any hex color:
```python
widget.set_color("#00ff00")  # Any hex value
```

## 💻 Complete Example

```python
from PyQt5 import QtWidgets
from pylcars import Lcars, Bracket, Slider, Textline, Colors

class MyApp:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.window = Lcars()
        self.window.setWindowTitle("My LCARS App")
        self.setup_widgets()

    def setup_widgets(self):
        central = self.window.centralwidget

        # Title
        title = Textline(central)
        title.setText("CONTROL PANEL")
        title.set_color(Colors.leuchtblau)
        title.setGeometry(50, 20, 700, 40)

        # Power slider
        label = Textline(central)
        label.setText("Power:")
        label.set_color(Colors.beige)
        label.setGeometry(50, 80, 100, 30)

        slider = Slider(central)
        slider.set_color(Colors.orange)
        slider.setRange(0, 100)
        slider.setGeometry(160, 80, 400, 40)
        slider.valueChanged.connect(self.on_power_changed)

        # Power value display
        self.power_display = Textline(central)
        self.power_display.set_color(Colors.hellorange)
        self.power_display.setGeometry(570, 80, 100, 30)

        # Control button
        button = Bracket(central)
        button.setText("ACTIVATE")
        button.set_color(Colors.orange)
        button.setGeometry(50, 150, 150, 50)
        button.clicked.connect(self.on_activate)

    def on_power_changed(self, value):
        self.power_display.setText(f"{value}%")

    def on_activate(self):
        print("Activated!")
        self.power_display.tickle(Colors.orange)

    def run(self):
        self.window.show()
        self.app.exec_()

if __name__ == "__main__":
    MyApp().run()
```

## 🔊 Audio Support

```python
from pylcars import Lcars

window = Lcars()
window.set_play_sound(True)
window.set_sound_file("path/to/sound.wav")
window.play_sound()
```

Connect audio to button clicks:

```python
button = Bracket(window.centralwidget)
button.clicked.connect(lambda: window.play_sound())
```

## 🏗️ Project Structure

```
pylcars/
├── __init__.py              # Package exports
├── lcars.py                 # Main window class
├── sound.py                 # Audio playback
├── colors.py                # LCARS color palette
├── conditions.py            # Status conditions
├── enumeration.py           # Base enumeration
├── orientation.py           # Direction constants
├── config.py                # Configuration constants
├── widgets/                 # Widget components
│   ├── __init__.py
│   ├── widgets.py           # Base widget class
│   ├── bracket.py           # Button widget
│   ├── block.py             # Rectangle widget
│   ├── deco.py              # Decorative label
│   ├── separator.py         # Divider widget
│   ├── slider.py            # Slider control
│   ├── textline.py          # Text label
│   ├── updown.py            # Navigation control
│   ├── menue.py             # Menu system
│   └── semicircle.py        # Rounded bracket
└── demos/                   # Example applications
    ├── simple_window.py     # Minimal example
    ├── colors_showcase.py   # Color palette
    ├── widgets_showcase.py  # All widgets
    ├── custom_theme.py      # Custom styling
    ├── menu.py              # Interactive demo
    └── sounds.py            # Audio demo
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed system design.

## 🧪 Development

### Setting Up for Development

```bash
# Clone and install
git clone https://github.com/StowasserH/pylcars.git
cd pylcars

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install with development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# With coverage
pytest tests/ --cov=pylcars --cov-report=term-missing

# Type checking
mypy pylcars/

# Code style
flake8 pylcars/
```

### Code Quality Standards

- **Type Hints**: All functions must have parameter and return type hints
- **Docstrings**: Google-style docstrings for all public APIs
- **Testing**: New features should include tests
- **Style**: PEP 8 compliance (100 char line length)
- **Coverage**: Aim for >70% code coverage

## 🐛 Troubleshooting

### Audio not working
- Ensure PortAudio is installed: `sudo apt-get install portaudio19-dev`
- Test PyAudio: `python -c "import pyaudio; print(pyaudio.__version__)"`

### PyQt5 import errors
- Reinstall: `pip install --upgrade PyQt5`
- Or use system package: `sudo apt-get install python3-pyqt5`

### Window won't display
- Ensure you call `window.show()` before `app.exec_()`
- Check that widgets have explicit `.setGeometry()` calls

### Widgets invisible
- All widgets need explicit positioning: `widget.setGeometry(x, y, w, h)`
- Default size is 0, so they won't appear without geometry

## 📚 Learning Resources

- [USAGE.md](USAGE.md) - Comprehensive usage guide with code examples
- [ARCHITECTURE.md](ARCHITECTURE.md) - Design documentation and system architecture
- [CONTRIBUTING.md](CONTRIBUTING.md) - Development guidelines
- `pylcars/demos/` - Working example applications
- Docstrings in source code - Class and method documentation

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Development setup
- Code style guidelines
- Testing requirements
- Pull request process

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Star Trek** - For the iconic LCARS aesthetic
- **PyQt5** - The GUI framework that makes this possible
- **Contributors** - Everyone who has contributed to this project

## 🔗 Links

- [GitHub Repository](https://github.com/StowasserH/pylcars)
- [Bug Reports & Issues](https://github.com/StowasserH/pylcars/issues)
- [Discussions](https://github.com/StowasserH/pylcars/discussions)
- [Star Trek Official](https://www.startrek.com/)

## 🎯 Project Status

| Aspect | Status |
|--------|--------|
| Development | ✅ Active |
| Version | 0.1.0 |
| Python Support | 3.8, 3.9, 3.10, 3.11, 3.12 |
| Tests | ✅ Passing |
| Documentation | ✅ Complete |
| Type Hints | ✅ 100% |
| CI/CD | ✅ GitHub Actions |

## 📋 Roadmap

- [ ] More widget types (progress bars, indicators)
- [ ] Advanced animations and transitions
- [ ] Theme system with loadable theme files
- [ ] Extended audio format support
- [ ] Performance optimizations
- [ ] PyPI publishing
- [ ] More demo applications
- [ ] Video tutorials

---

**Ready to build something legendary? Start with the [Usage Guide](USAGE.md)!** 🚀

*May your interfaces be bold and your colors be vivid!* 🖖
