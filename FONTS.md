# Installing LCARS and Star Trek Fonts

PyLCARS includes intelligent font fallback, so it works even without the LCARS font. However, for the authentic Star Trek aesthetic, installing LCARS fonts is recommended.

## About the Fonts

For copyright reasons, LCARS fonts are not included with PyLCARS. However, they are freely available from fan communities and are widely used in Star Trek fan projects.

**Popular LCARS fonts:**
- `lcars.ttf` - Classic LCARS design
- `LCARSGTJ2.ttf` - Alternative LCARS style
- Other Star Trek fonts: Klingon, Ferengi, DS9, TNG fonts

These fonts are available from:
- GitHub repositories (search: "LCARS font", "Star Trek fonts")
- Star Trek fan communities and forums
- Font archives with Star Trek collections

## Installation

### Linux / macOS

1. **Download** the LCARS font file (.ttf)

2. **Create the fonts directory** (if it doesn't exist)
   ```bash
   mkdir -p ~/.local/share/fonts
   ```

3. **Copy the font file**
   ```bash
   cp lcars.ttf ~/.local/share/fonts/
   # Or for multiple fonts:
   cp *.ttf ~/.local/share/fonts/
   ```

4. **Rebuild the font cache**
   ```bash
   fc-cache -f ~/.local/share/fonts
   ```

5. **Verify installation**
   ```bash
   fc-list | grep -i lcars
   ```

6. **Restart your application**
   ```bash
   python -m pylcars.demos.menu
   ```

### Windows

1. **Download** the LCARS font file (.ttf)

2. **Install the font**
   - Right-click on the .ttf file
   - Select "Install"
   - Or: Open **Settings** → **Personalization** → **Fonts** → Drag and drop the .ttf file

3. **Restart your application**

### System-Wide Installation (All Users)

**Linux:**
```bash
sudo cp lcars.ttf /usr/share/fonts/
sudo fc-cache -f /usr/share/fonts/
```

**macOS:**
```bash
cp lcars.ttf /Library/Fonts/
```

**Windows (Admin):**
- Copy .ttf file to `C:\Windows\Fonts\`

## Verifying Installation

After installation, the font should automatically be used by PyLCARS.

**Check if LCARS font is in use:**
```python
from PyQt5 import QtWidgets
from pylcars import Lcars, Bracket

app = QtWidgets.QApplication([])
window = Lcars()
button = Bracket(window.centralwidget)

if not button.is_using_fallback_font():
    print("✅ LCARS font is installed and in use!")
else:
    print("⚠️  Using fallback font (LCARS not found)")
```

## Fallback Font

If the LCARS font is not installed, PyLCARS automatically uses **Courier 18pt** as a fallback. This provides a working alternative while maintaining usability.

A warning message is displayed when the application starts if the LCARS font is not available:

```
======================================================================
⚠️  WARNING: LCARS font not found!
======================================================================
The 'LCARS' font is not installed on this system.
Using fallback 'Courier' font at 18pt instead.

📝 To install the LCARS font:
  ...
```

## Troubleshooting

### Font not found after installation

1. **Check if the file was copied correctly**
   ```bash
   ls ~/.local/share/fonts/ | grep -i lcars
   ```

2. **Rebuild the font cache**
   ```bash
   fc-cache -f ~/.local/share/fonts
   ```

3. **Verify font is readable**
   ```bash
   file ~/.local/share/fonts/lcars.ttf
   ```

4. **Check font name**
   ```bash
   fc-query ~/.local/share/fonts/lcars.ttf | grep "family:"
   ```

   The family name should be "LCARS" (exact match required)

5. **On Linux, try updating all font caches**
   ```bash
   fc-cache
   ```

### Font name mismatch

PyLCARS looks for a font named exactly **"LCARS"**. If your font file has a different internal name, you may need to:

1. Check the font name:
   ```bash
   fc-query path/to/font.ttf | grep "family:"
   ```

2. Use a different font with the correct name, or

3. Manually select a different font in your application:
   ```python
   from PyQt5 import QtGui
   button.set_default_font("Your Font Name", 26)
   ```

## Other Star Trek Fonts

PyLCARS supports any installed font. You can use other Star Trek fonts by specifying the font name:

```python
from PyQt5 import QtGui
from pylcars import Bracket

button = Bracket(window.centralwidget)
button.set_default_font("Klingon", 24)  # If installed
```

Common Star Trek fonts:
- `LCARS` - LCARS UI font
- `Klingon` - Klingon script
- `Ferengi` - Ferengi script
- `DS9` - Deep Space Nine font
- `TNG` - The Next Generation font

## Resources

- **Star Trek Fonts**: Search GitHub for "LCARS font" or "Star Trek fonts"
- **Font Installation Help**: `fc-cache` documentation or system font settings
- **PyLCARS Documentation**: See [USAGE.md](USAGE.md) for font configuration examples

---

**May your interfaces be legendary!** 🖖
