# Contributing to Semantic Kernel Agent Demonstrations

Thank you for your interest in contributing to this project! We welcome contributions from the community.

## 👤 Project Maintainer

**Ramkumar JD**  
REDIVAC Technologies

## 🤝 How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:

1. **Check existing issues** - Search to see if it's already reported
2. **Create a new issue** - Provide detailed information:
   - Clear description of the problem or suggestion
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Environment details (Python version, OS, etc.)
   - Error messages or screenshots

### Submitting Changes

We follow a standard GitHub workflow:

1. **Fork the repository**
   ```bash
   git clone https://github.com/your-username/SKPlanners.git
   cd SKPlanners
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the coding standards below
   - Add tests if applicable
   - Update documentation

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: Brief description of your changes"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**
   - Provide clear description of changes
   - Reference any related issues
   - Explain the benefit of your changes

## 📝 Coding Standards

### Python Code Style

- Follow [PEP 8](https://pep8.org/) style guide
- Use meaningful variable and function names
- Add docstrings to classes and functions
- Keep functions focused and concise
- Maximum line length: 100 characters

Example:
```python
class MyPlugin:
    """
    Brief description of the plugin.
    
    More detailed explanation if needed.
    """
    
    @kernel_function(
        name="my_function",
        description="Clear description for the AI to understand"
    )
    def my_function(self, param: str) -> str:
        """
        Brief description of what this function does.
        
        Args:
            param: Description of the parameter
            
        Returns:
            Description of the return value
        """
        result = f"Processed: {param}"
        return result
```

### Plugin Development Guidelines

1. **Clear Descriptions** - Write descriptions that help the AI understand when to use the function
2. **Type Hints** - Always use type hints for parameters and return values
3. **Error Handling** - Handle edge cases gracefully
4. **Logging** - Use print statements or logging for debugging
5. **Documentation** - Add docstrings and comments

### Notebook Guidelines

1. **Markdown Cells** - Use clear headings and explanations
2. **Code Organization** - One concept per cell
3. **Output Clarity** - Show meaningful results
4. **Dependencies** - List all required imports at the top
5. **Path Handling** - Handle relative paths correctly

### Commit Message Format

Use clear, descriptive commit messages:

```
Add: New feature or functionality
Fix: Bug fix
Update: Modification to existing feature
Refactor: Code restructuring without changing behavior
Docs: Documentation changes
Test: Adding or updating tests
```

Examples:
```
Add: WeatherPlugin for destination temperatures
Fix: Import path issue in notebooks
Update: Improve error handling in agent demo
Docs: Add troubleshooting section to README
```

## 🔍 Code Review Process

1. All pull requests require review before merging
2. Reviewers will check:
   - Code quality and style
   - Functionality and correctness
   - Documentation completeness
   - Test coverage (if applicable)
   - Compatibility with existing code

3. Address feedback promptly
4. Update PR based on review comments

## 🧪 Testing

When adding new features:

1. Test manually with different scenarios
2. Test with Azure OpenAI integration
3. Verify notebook execution (if applicable)
4. Check error handling and edge cases

## 📚 Documentation

Update documentation when you:

- Add new plugins or features
- Change existing functionality
- Add new notebooks or demos
- Modify setup or configuration

Required documentation updates:

- **README.md** - For user-facing changes
- **Docstrings** - For code-level documentation
- **Notebooks** - For interactive examples
- **Comments** - For complex logic

## 🎯 What We're Looking For

### High Priority

- New plugin implementations for common use cases
- Enterprise scenario demonstrations
- Performance improvements
- Better error handling
- Documentation improvements
- Bug fixes

### Ideas for Contributions

- **Plugins**
  - Email processing plugin
  - Database query plugin
  - File operations plugin
  - Web scraping plugin
  
- **Demos**
  - Multi-agent collaboration
  - Memory and context management
  - Custom connector implementations
  - Integration with external APIs

- **Notebooks**
  - Advanced RAG patterns
  - Agent orchestration patterns
  - Production deployment guides
  - Performance optimization

- **Documentation**
  - Video tutorials
  - Architecture diagrams
  - Best practices guide
  - Troubleshooting guides

## 🚫 What to Avoid

- Breaking changes without discussion
- Large refactors without prior approval
- Adding dependencies without justification
- Removing existing functionality
- Code without documentation
- Untested changes

## 💬 Getting Help

If you need help with your contribution:

1. **Open an issue** - Describe what you want to work on
2. **Ask questions** - Don't hesitate to ask for clarification
3. **Share early** - Create draft PRs to get feedback
4. **Be patient** - Reviews may take time

## 📜 Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome diverse perspectives
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discriminatory language
- Personal attacks or insults
- Publishing others' private information
- Other unprofessional conduct

## 📧 Contact

For questions or concerns about contributing:

- **Email**: [Provide contact email]
- **GitHub Issues**: For technical questions
- **Pull Requests**: For code discussions

## 🙏 Recognition

Contributors will be recognized in:

- README.md contributors section
- Release notes
- Project documentation

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping make this project better! Your contributions are valuable and appreciated.

**Happy Contributing! 🎉**
