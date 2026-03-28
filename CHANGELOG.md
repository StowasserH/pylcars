# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-03-28

### Added

- ✨ Comprehensive test suite with pytest
  - 12 basic smoke tests covering imports and enumerations
  - pytest configuration with proper markers
  - Test fixtures for PyQt5 QApplication and main window

- 🔄 GitHub Actions CI/CD pipeline
  - Automated testing on Python 3.8, 3.10, 3.11, 3.12
  - Code quality checks (flake8, mypy)
  - Coverage reporting with codecov integration
  - Daily scheduled test runs

- 📝 Type hints across all modules
  - Complete parameter and return type annotations
  - PyQt5 type hints for better IDE support
  - Support for optional and complex types (Dict, List, Callable)

- 📚 Comprehensive API documentation
  - Google-style docstrings for all modules, classes, and public methods
  - Detailed parameter and return value documentation
  - Exception documentation

- 🛠️ Configuration system
  - Centralized configuration constants in `pylcars/config.py`
  - Constants for window size, audio chunk size, animation timing
  - Easy tuning without code modifications

- 📋 Development documentation
  - Expanded README with features, quick start, and examples
  - CONTRIBUTING.md with development guidelines
  - Code style and docstring format specifications
  - Testing and code quality standards

- 🏗️ Modern packaging
  - pyproject.toml with PEP 621 format
  - Proper package discovery with find_packages()
  - Python 3.8+ requirement specification
  - Development dependencies group

### Fixed

- 🐛 Critical memory leak issues in audio playback
  - Fixed list modification during iteration in sound cleanup
  - Proper wave file handling and resource closure
  - Added error handling for file operations
  - Improved stream cleanup in __del__ method
  - Graceful exception handling in audio initialization

- 🔧 Package structure issues
  - Fixed subpackage discovery (pylcars.widgets)
  - Corrected setup.py with find_packages()
  - Proper Python version constraint

- 🧹 Code quality and consistency
  - Removed all commented-out code
  - Removed PyQt4 compatibility shims (_fromUtf8, _translate)
  - Consistent method naming (setPlay_sound → set_play_sound)
  - Removed unused joke() function

### Changed

- ♻️ Legacy code modernization
  - Removed PyQt4-era compatibility functions
  - Simplified string handling for PyQt5
  - Removed unnecessary commented stylesheet code

- 📦 Dependency management
  - Explicit dependency specification in pyproject.toml
  - Separated development dependencies
  - Added test framework requirements (pytest, pytest-cov, pytest-qt)

### Improved

- 🎯 Project structure clarity
  - Added __all__ exports for explicit public API
  - Better module organization
  - Clearer configuration management

- 📊 Code maintainability
  - Extracted magic numbers to named constants
  - Improved documentation across all files
  - Enhanced IDE support with type hints

## [0.0.1] - Previous Releases

See git history for changes in earlier versions.

---

## How to Upgrade

### From 0.0.1 to 0.1.0

The 0.1.0 release includes breaking changes:

1. **Method rename**: `setPlay_sound()` → `set_play_sound()`
   - Update any calls to the Sound class method
   ```python
   # Old
   lcars_window.setPlay_sound(True)

   # New
   lcars_window.set_play_sound(True)
   ```

2. **Dependency updates**: Ensure PyQt5 is properly installed
   ```bash
   pip install --upgrade PyQt5 pylcars
   ```

3. **Configuration**: If you've customized window sizes, consider using the new config constants
   ```python
   from pylcars.config import DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT
   ```

## Future Roadmap

- [ ] More widget types (progress bars, status indicators, etc.)
- [ ] Advanced animation effects
- [ ] Theme system with custom color schemes
- [ ] Better audio support (more formats, mixing)
- [ ] Performance optimizations
- [ ] Extended documentation and tutorials
- [ ] Demo applications gallery
- [ ] PyPI package publishing

## Known Issues

None at this time. Please report any issues on [GitHub Issues](https://github.com/StowasserH/pylcars/issues).

## Support

For questions and issues:
- Open an issue on [GitHub](https://github.com/StowasserH/pylcars/issues)
- Check existing documentation in CONTRIBUTING.md
- Review demo applications for usage examples
