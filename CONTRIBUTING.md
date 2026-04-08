# Contributing to Arcshift

Thank you for your interest in contributing to Arcshift! This project is a Copilot-driven app modernisation accelerator for SI/Partners.

## How to Contribute

### Reporting Issues
- Use GitHub Issues for bugs, feature requests, or questions
- Include the phase/agent/skill affected and steps to reproduce

### Pull Requests
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes following the conventions below
4. Commit with conventional commits: `feat:`, `fix:`, `docs:`, `chore:`
5. Push and open a Pull Request

### Conventions

**Copilot Agents** (`.github/agents/`)
- One agent per modernisation phase
- Use minimal tool sets (principle of least privilege)
- Include clear constraints and output format sections

**Copilot Skills** (`.github/skills/`)
- Folder name must match the `name` field in SKILL.md frontmatter
- Keep SKILL.md under 500 lines; use `references/` for detailed docs
- Include step-by-step procedures, not just descriptions

**Prompts** (`.github/prompts/`)
- One focused task per prompt
- Use `{{variables}}` for parameterised inputs
- Include example usage in the prompt body

**Methodology** (`methodology/`)
- Each phase has its own directory with a README.md
- Include Copilot integration points (which agent/skill to use)
- Provide checklists and decision trees

**Sample Apps** (`samples/`)
- `before/` = realistic legacy patterns (not clean code)
- `after/` = modernised equivalent demonstrating target patterns
- Keep as representative skeletons, not full production apps

**IaC** (`infra/`)
- Modular: one resource type per module
- Parameterised with sensible defaults
- Both Bicep and Terraform for the same resources

**Patterns** (`patterns/`)
- Include: problem, context, solution, implementation steps, trade-offs
- Reference which Arcshift agents/skills implement the pattern

## Code of Conduct

Be respectful, constructive, and inclusive. We follow the [Contributor Covenant](https://www.contributor-covenant.org/).

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
