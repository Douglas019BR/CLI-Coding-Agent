from pydantic_ai.mcp import MCPServerStdio

run_python = MCPServerStdio(
    "deno",
    args=[
        "run",
        "-N",
        "-R=node_modules",
        "-W=node_modules",
        "--node-modules-dir=auto",
        "jsr:@pydantic/mcp-run-python",
        "stdio",
    ],
)

internet_search = MCPServerStdio(command="duckduckgo-mcp-server", args=[], timeout=60)

code_reasoning = MCPServerStdio(
    command="npx",
    args=["-y", "@mettamatt/code-reasoning"],
    tool_prefix="code_reasoning",
)

desktop_commander = MCPServerStdio(
    command="npx",
    args=["-y", "@wonderwhy-er/desktop-commander"],
    tool_prefix="desktop_commander",
    timeout=60,
)

# AWS MCP servers - commented out because they require 'uv' instead of 'python -m'
# To use these, install uv (curl -LsSf https://astral.sh/uv/install.sh | sh) and change to:
# awslabs = MCPServerStdio(command="uvx", args=["awslabs.core-mcp-server@latest"], ...)
# aws_docs = MCPServerStdio(command="uvx", args=["awslabs.aws-documentation-mcp-server@latest"], ...)

# awslabs = MCPServerStdio(
#     command="python",
#     args=["-m", "awslabs.core_mcp_server"],
#     env={"FASTMCP_LOG_LEVEL": "ERROR"},
#     tool_prefix="awslabs",
# )

# aws_docs = MCPServerStdio(
#     command="python",
#     args=["-m", "awslabs.aws_documentation_mcp_server"],
#     env={"FASTMCP_LOG_LEVEL": "ERROR", "AWS_DOCUMENTATION_PARTITION": "aws"},
#     tool_prefix="aws_docs",
# )

context7 = MCPServerStdio(
    command="npx", args=["-y", "@upstash/context7-mcp"], tool_prefix="context"
)

MCP_SERVERS = [
    run_python,
    internet_search,
    code_reasoning,
    context7,
    desktop_commander,
]
