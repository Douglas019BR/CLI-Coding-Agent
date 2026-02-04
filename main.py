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

    @agent.tool_plain()
    def run_unit_tests() -> str:
        """Run unit tests using pytest."""
        result = subprocess.run(
            ["python", "-m", "pytest", "-xvs", "tests/"], capture_output=True, text=True
        )
        return result.stdout

    return agent


async def main():
    agent = create_agent()
    async with agent.run_mcp_servers():
        await agent.to_cli()


if __name__ == "__main__":
    asyncio.run(main())
