# CLI-Coding-Agent
My own CLI Coding Agent based on PydanticAI

## Inspiration

This project was inspired by the excellent article ["Building your own CLI Coding Agent with Pydantic-AI"](https://martinfowler.com/articles/build-own-coding-agent.html) by Ben O'Mahony. Special thanks to Ben O'Mahony for the detailed guide and to Martin Fowler's blog for publishing such valuable content.

I made some changes to run without UV and to organize the repository in my own way.

## Prerequisites

### Deno
```bash
curl -fsSL https://deno.land/install.sh | sh
```

### Node.js and npm
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install nodejs npm

# macOS
brew install node
```

### pipx
```bash
pip install pipx
```

## Installation

1. Clone the repository
2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Additional Features

This implementation includes several enhancements beyond the original tutorial:

### Code Organization
- **Modular structure**: MCP servers separated into `mcp_servers.py`
- **Instructions externalized**: Agent instructions in `instructions.py`
- **Color-coded interface**: Enhanced CLI with colored output and startup information

### Built-in Tools
The agent includes essential file system and command execution tools:
- `read_file()` - Read file contents
- `write_file()` - Create/modify files  
- `list_directory()` - List directory contents
- `run_command()` - Execute shell commands in current directory
- `run_unit_tests()` - Run pytest tests

### MCP Server Configuration
- **Timeout handling**: Increased timeouts for MCP servers that need more initialization time
- **Compatibility fixes**: Removed MCP servers incompatible with AWS Bedrock schema validation
- **Dependency management**: Uses pip/pipx instead of UV for easier setup

### Active MCP Servers
- **run_python**: Execute Python code via Deno
- **internet_search**: DuckDuckGo search capabilities  
- **context7**: Context management and documentation
- **desktop_commander**: Desktop automation tools

### AWS Bedrock Compatibility
- Configured for AWS Bedrock with Amazon Nova model
- Schema validation compatible with Bedrock requirements
- Proper error handling for model-specific limitations
