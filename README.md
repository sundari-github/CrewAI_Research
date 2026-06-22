# CrewAI Research Project

A multi-agent AI research system built with [CrewAI](https://github.com/joaomdmoura/crewai) that autonomously researches topics and generates comprehensive reports.

## Features

- **Multi-Agent System**: Orchestrated AI agents working collaboratively to research and analyze topics
- **Custom Tools**: Email sending and specialized research tools for enhanced capabilities
- **Report Generation**: Automatically generates detailed research reports in markdown format
- **Knowledge Management**: Stores and manages user preferences and research data
- **Configurable Workflows**: Easy-to-customize agent and task configurations via YAML

## Project Structure

```
research_crew/
├── src/
│   └── research_crew/
│       ├── crew.py              # Main crew orchestration
│       ├── main.py              # Entry point
│       ├── config/
│       │   ├── agents.yaml       # Agent definitions
│       │   └── tasks.yaml        # Task definitions
│       └── tools/
│           ├── custom_tool.py    # Custom research tools
│           └── email_sending_tool.py  # Email functionality
├── knowledge/
│   └── user_preference.txt       # User preferences and settings
├── tests/                        # Test suite
├── pyproject.toml                # Project metadata and dependencies
└── env.config                    # Configuration file (not tracked in git)
```

## Prerequisites

- Python 3.10+
- Poetry or pip for package management
- OpenAI API key (for LLM functionality)

## Installation

### Using Poetry

```bash
cd research_crew
poetry install
```

### Using pip

```bash
pip install -r Requirements.txt
```

## Configuration

1. Create an `env.config` file in the `research_crew` directory:

```
OPENAI_API_KEY=your_api_key_here
```

2. Update user preferences in `knowledge/user_preference.txt` to customize research parameters

## Usage

### Running the Crew

```bash
python -m research_crew.main
```

Or directly:

```bash
cd research_crew
python src/research_crew/main.py
```

### Example Topics

The system can research various topics including:
- AI For Testing
- AI News
- AI Fatigue
- Responsible AI
- Software Testing
- And more...

### Output

Research reports are generated as markdown files (`*_report.md`) in the `research_crew` directory.

## Configuration Files

### agents.yaml
Defines the AI agents, their roles, and capabilities.

### tasks.yaml
Specifies the research tasks, objectives, and agent assignments.

## Development

### Running Tests

```bash
pytest tests/
```

### Project Structure Notes

- **src/**: Source code for the crew application
- **tests/**: Unit and integration tests
- **knowledge/**: Persistent knowledge and user data
- **reports/**: Generated research reports (markdown files)

## Customization

### Adding New Tools

Create new tool files in `src/research_crew/tools/` and import them in the crew configuration.

### Modifying Agents

Edit `config/agents.yaml` to add, modify, or remove agents and their properties.

### Updating Tasks

Edit `config/tasks.yaml` to change task definitions, descriptions, and agent assignments.

## Requirements

See `Requirements.txt` for a complete list of dependencies.

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required for LLM functionality)

## Notes

- `env.config` is excluded from version control to protect sensitive information
- Generated reports are excluded from version control (can be added on a need basis)
- Virtual environments are configured in `.gitignore`

## Contributing

Feel free to extend this project with new agents, tools, and research capabilities.

## License

MIT License

## Support

For issues or questions about CrewAI, visit the [official repository](https://github.com/joaomdmoura/crewai).
