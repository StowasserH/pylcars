# Contributing to PyLCARS

First off, thank you for considering contributing to PyLCARS! It's people like you that make PyLCARS such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps which reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed after following the steps**
- **Explain which behavior you expected to see instead and why**
- **Include screenshots and animated GIFs if possible**
- **Include your environment details** (OS, Python version, PyQt5 version)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior and the expected enhancement**
- **Explain why this enhancement would be useful**

### Pull Requests

- Fill in the required template
- Follow the Python styleguides
- Include appropriate test cases
- Update documentation as needed
- End all files with a newline
- Avoid platform-dependent code

## Development Setup

### Prerequisites

- Python 3.8+
- Git
- Virtual environment tool (`.venv`)

### Setting Up Your Development Environment

1. **Fork the repository**

   ```bash
   git clone https://github.com/your-username/pylcars.git
   cd pylcars
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install development dependencies**

   ```bash
   pip install -e ".[dev]"
   ```

4. **Verify installation**

   ```bash
   pytest tests/ -v
   ```

### Making Changes

1. **Create a feature branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** and commit them regularly

3. **Run tests locally**

   ```bash
   pytest tests/ -v --cov=pylcars
   ```

4. **Check code quality**

   ```bash
   flake8 pylcars/
   mypy pylcars/ --ignore-missing-imports
   ```

5. **Format your code**

   ```bash
   black pylcars/ tests/
   ```

## Styleguides

### Python Code Style

We follow **PEP 8** with these additional guidelines:

- **Line length**: Maximum 100 characters
- **Type hints**: All functions and methods must have type hints for parameters and return values
- **Docstrings**: All public classes and methods must have docstrings in Google style format
- **Imports**: Use absolute imports where possible

#### Example:

```python
from typing import Optional, List

def process_items(items: List[str], separator: Optional[str] = None) -> str:
    """Process a list of items into a string.

    Args:
        items: List of string items to process.
        separator: String to use between items (default: comma).

    Returns:
        Processed string with items joined by separator.

    Raises:
        ValueError: If items list is empty.
    """
    if not items:
        raise ValueError("Items list cannot be empty")

    sep = separator or ", "
    return sep.join(items)
```

### Docstring Format

We use **Google-style docstrings**:

```python
"""Brief description.

Longer description that explains what this function/class does.
Can span multiple lines.

Args:
    param1: Description of param1.
    param2: Description of param2 (default: None).

Returns:
    Description of return value.

Raises:
    ExceptionType: Description of when this exception is raised.
"""
```

### Commit Messages

- Use the imperative mood ("add feature" not "added feature")
- Use the present tense ("move cursor to..." not "moved cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line
- Consider starting the commit message with an applicable emoji:
  - 🎨 `:art:` Improve structure/format
  - 🐛 `:bug:` Fix a bug
  - ✨ `:sparkles:` Add a new feature
  - 📚 `:books:` Documentation update
  - 🧪 `:test_tube:` Add tests
  - ♻️ `:recycle:` Refactor code
  - 🚀 `:rocket:` Performance improvement
  - ⚙️ `:gear:` Configuration/setup

## Testing

### Writing Tests

- Place new test files in the `tests/` directory
- Name test files as `test_*.py`
- Use `pytest` as the testing framework
- Write descriptive test names that explain what is being tested
- Include docstrings explaining the test intent

Example test:

```python
def test_colors_exist() -> None:
    """Test that color constants are defined."""
    assert hasattr(Colors, "orange")
    assert hasattr(Colors, "flieder")
```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=pylcars --cov-report=term-missing

# Run specific test
pytest tests/test_colors.py::test_colors_exist -v

# Run tests matching pattern
pytest tests/ -k "color" -v
```

### Coverage Requirements

- Aim for **>70% code coverage**
- All public APIs should be tested
- Document any untestable code with comments

## Documentation

### Updating Documentation

1. Update docstrings in the code
2. Update relevant `.md` files
3. Update CHANGELOG.md if adding user-facing changes

### Building Documentation

```bash
# Generate documentation
sphinx-build -b html docs/ docs/_build/
```

## Additional Notes

### Issue and Pull Request Labels

We use labels to categorize issues and PRs:

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements or additions to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `question` - Further information is requested
- `wontfix` - This will not be worked on

## Recognition

Contributors will be recognized in:
- GitHub contributors page
- CHANGELOG.md
- README.md (for significant contributions)

## Questions?

Feel free to open an issue with the label `question` or contact the maintainers directly.

Thank you for contributing! 🚀
