import asyncio


import subprocess
import boto3
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio
from pydantic_ai.models.bedrock import BedrockConverseModel
from pydantic_ai.providers.bedrock import BedrockProvider
from botocore.config import Config as BotocoreConfig

from instructions import INSTRUCTIONS
from mcp_servers import MCP_SERVERS

# Códigos de cor ANSI
class Colors:
    CYAN = '\033[1;36m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    RED = '\033[1;31m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


def create_agent():
    """Create and configure the CLI agent"""
    bedrock_config = BotocoreConfig(
        read_timeout=300,
        connect_timeout=60,
        retries={"max_attempts": 3},
    )

    bedrock_client = boto3.client(
        "bedrock-runtime", region_name="us-east-1", config=bedrock_config
    )

    model = BedrockConverseModel(
        "amazon.nova-micro-v1:0",
        provider=BedrockProvider(bedrock_client=bedrock_client),
    )

    agent = Agent(
        model=model,
        instructions=INSTRUCTIONS,
        mcp_servers=MCP_SERVERS,
    )
    
    # Personalizar a interface com cores e informações
    print(f"\n{Colors.BOLD}{Colors.CYAN}🤖 CLI Coding Agent Iniciado{Colors.RESET}")
    print(f"{Colors.YELLOW}Modelo: {Colors.RESET}amazon.nova-micro-v1:0")
    print(f"{Colors.YELLOW}MCPs ativos: {Colors.RESET}{len(MCP_SERVERS)}")
    print(f"{Colors.GREEN}Digite 'exit' ou 'quit' para sair{Colors.RESET}\n")
    
    return agent
    agent._cli_name = "\033[1;36mpydantic-ai\033[0m"  # Ciano bold

    @agent.tool_plain()
    def run_unit_tests() -> str:
        """Run unit tests using pytest."""
        result = subprocess.run(
            ["python", "-m", "pytest", "-xvs", "tests/"], capture_output=True, text=True
        )
        return result.stdout
    
    @agent.tool_plain()
    def read_file(file_path: str) -> str:
        """Read contents of a file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {str(e)}"
    
    @agent.tool_plain()
    def write_file(file_path: str, content: str) -> str:
        """Write content to a file."""
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return f"Successfully wrote to {file_path}"
        except Exception as e:
            return f"Error writing file: {str(e)}"
    
    @agent.tool_plain()
    def list_directory(directory_path: str = ".") -> str:
        """List contents of a directory."""
        try:
            import os
            files = os.listdir(directory_path)
            return "\n".join(files)
        except Exception as e:
            return f"Error listing directory: {str(e)}"
    
    @agent.tool_plain()
    def run_command(command: str) -> str:
        """Execute a shell command in the current working directory."""
        try:
            import os
            current_dir = os.getcwd()
            result = subprocess.run(
                command, 
                shell=True, 
                capture_output=True, 
                text=True, 
                timeout=30,
                cwd=current_dir
            )
            return f"Working directory: {current_dir}\nExit code: {result.returncode}\nStdout:\n{result.stdout}\nStderr:\n{result.stderr}"
        except Exception as e:
            return f"Error running command: {str(e)}"
            result = subprocess.run(
                command, 
                shell=True, 
                capture_output=True, 
                text=True, 
                timeout=30,
                cwd=working_dir
            )
            return f"Working directory: {working_dir}\nExit code: {result.returncode}\nStdout:\n{result.stdout}\nStderr:\n{result.stderr}"
        except Exception as e:
            return f"Error running command: {str(e)}"

    return agent


async def main():
    agent = create_agent()
    async with agent.run_mcp_servers():
        await agent.to_cli()


if __name__ == "__main__":
    asyncio.run(main())
