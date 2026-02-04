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

internet_search = MCPServerStdio(command="uvx", args=["duckduckgo-mcp-server"])

code_reasoning = MCPServerStdio(
    command="npx",
    args=["-y", "@mettamatt/code-reasoning"],
    tool_prefix="code_reasoning",
)

desktop_commander = MCPServerStdio(
    command="npx",
    args=["-y", "@wonderwhy-er/desktop-commander"],
    tool_prefix="desktop_commander",
)

awslabs = MCPServerStdio(
    command="uvx",
    args=["awslabs.core-mcp-server@latest"],
    env={"FASTMCP_LOG_LEVEL": "ERROR"},
    tool_prefix="awslabs",
)

aws_docs = MCPServerStdio(
    command="uvx",
    args=["awslabs.aws-documentation-mcp-server@latest"],
    env={"FASTMCP_LOG_LEVEL": "ERROR", "AWS_DOCUMENTATION_PARTITION": "aws"},
    tool_prefix="aws_docs",
)

context7 = MCPServerStdio(
    command="npx", args=["-y", "@upstash/context7-mcp"], tool_prefix="context"
)

MCP_SERVERS = [
    run_python,
    internet_search,
    code_reasoning,
    desktop_commander,
    awslabs,
    aws_docs,
    context7,
]
