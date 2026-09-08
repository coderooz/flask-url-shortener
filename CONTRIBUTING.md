# Contributing to Flask URL Shortener

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing.

## How to Contribute

### Reporting Bugs

1. Check existing issues to avoid duplicates
2. Open a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Python version and Flask version

### Suggesting Features

1. Open an issue with the `enhancement` label
2. Describe the feature and its use case
3. Explain why it would be valuable

### Submitting Changes

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Test thoroughly
5. Commit with a clear message
6. Push to your fork
7. Open a Pull Request

## Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/flask-url-shortener.git
cd flask-url-shortener

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

## Code Style

- Follow PEP 8 guidelines
- Keep functions small and focused
- Add comments for complex logic
- Use meaningful variable names

## Pull Request Guidelines

- One feature/fix per PR
- Include a clear description
- Update documentation if needed
- Ensure the app runs without errors

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
