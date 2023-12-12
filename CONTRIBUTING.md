# Contributing to FolderForge

Thank you for considering contributing to FolderForge! We appreciate your efforts to make this project better.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Code Contribution](#code-contribution)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guide](#style-guide)
- [Commit Message Guidelines](#commit-message-guidelines)
- [License](#license)

## Code of Conduct

This project and everyone participating in it are governed by the [FolderForge Code of Conduct](./CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [phd.sten.tech@gmail.com].

## How Can I Contribute?

### Reporting Bugs

- Before reporting a bug, check if it has already been reported in the [GitHub Issues](https://github.com/StenTech/FolderForge/issues).
- If not, open a new issue, providing a clear and detailed description of the bug and steps to reproduce it.

### Suggesting Enhancements

- Before suggesting an enhancement, check if it has already been suggested or implemented in the [GitHub Issues](https://github.com/StenTech/FolderForge/issues).
- If not, open a new issue, describing the enhancement you'd like to see and why it is valuable.

### Code Contribution

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Commit your changes following the [commit message guidelines](#commit-message-guidelines).
- Push your changes to your fork.
- Open a pull request against the main branch of the original repository.

## Development Setup

To set up FolderForge for local development, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your-username/FolderForge.git
cd FolderForge
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start contributing!

## Pull Request Process

1. Ensure your code follows the style guide.
2. Update the documentation if necessary.
3. Verify that your changes work locally.
4. Open a pull request, describing the changes and referencing any related issues.

## Style Guide

This style guide outlines the coding conventions and best practices for contributing to the FolderForge project.

### Naming Conventions

- Use `snake_case` for variable names.
- Use `PascalCase` (also known as UpperCamelCase) for class names.
- Use `camelCase` for function and method names.

### Indentation

- Indent using `tabs`.
- Use `4 spaces` for indentation.

### Code Organization

- Keep lines under 80 characters when possible.
- Use blank lines to separate logical sections of code.
- Group related functions and methods together.

### Documentation

- Write clear and concise comments.
- Use docstrings for functions and classes to provide documentation.

### Version Control

- Make atomic commits with clear and descriptive commit messages.
- Reference relevant issues and pull requests in commit messages.

### Testing

- Write unit tests for new features and bug fixes.
- Ensure all existing tests pass before creating a pull request.

#### Examples

**Variable Naming**

```python
# Good
user_name = "JohnDoe"
total_count = 100

# Bad
userName = "JohnDoe"
totalCount = 100
```

**Class Naming**

```python
# Good
class FolderForge:
    # class implementation

# Bad
class folderForge:
    # class implementation
```

**Function Naming**

```python
# Good
def calculate_total():
    # function implementation

# Bad
def calculateTotal():
    # function implementation
```

**Indentation**

Use tabs, no spaces for tabulation (4 spaces for tab )

```python
# Good
if condition:
    action()

# Bad
if condition:
  action()
```

**Code Organization**

```python
# Good
class MyClass:
    def method1(self):
        # method implementation

    def method2(self):
        # method implementation

# Bad
class MyClass:
    def method1(self):
        # method implementation
    def method2(self):
        # method implementation
```

**Documentation**

```python
# Good
def add_numbers(a, b):
    """
    Adds two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of a and b.
    """
    return a + b

# Bad
def add_numbers(a, b):
    return a + b
```

**Version Control**

```bash
# Good
git commit -m "Add feature: Implement folder creation functionality

This commit adds a new feature that allows the creation of folders
based on the provided configuration.
Closes #123."

# Bad
git commit -m "Fix bug"
```

Remember to follow these guidelines to maintain consistency across the project. Happy coding!

## Commit Message Guidelines
When making a commit, please follow these guidelines:

- Use the present tense ("Add feature" not "Added feature").
- Limit the first line to 72 characters or less.
- Reference relevant issues and pull requests in the commit message.

**Example:**

```
Add feature: Implement folder creation functionality

This commit adds a new feature that allows the creation of folders
based on the provided configuration.
Closes #123.
```

## License
By contributing, you agree that your contributions will be licensed under the [MIT License](./LICENSE).

Happy coding!