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
