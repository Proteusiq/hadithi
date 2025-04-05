from typer import prompt
from rich.console import Console
from rich.panel import Panel

from smolagents import CodeAgent, DuckDuckGoSearchTool, ToolCollection
from smolagents import LiteLLMModel

from mcp import StdioServerParameters

console = Console()


server_parameters = StdioServerParameters(
    command="uvx",
    args=["--quiet", "arxiv-mcp-server"],
    env={"UV_PYTHON": "3.12"},
)

model = LiteLLMModel(
    "anthropic/claude-3-7-sonnet-latest",
)

with ToolCollection.from_mcp(
    server_parameters=server_parameters, trust_remote_code=True
) as tool_collection:
    console.print(Panel("[bold blue]🙈 Exploring The World via MCP[/]", title="Starting agent 'Eloise'"))

    tool_info = "\n".join(
        [
            f"[bold]{tool.name}[/bold]: {tool.description}"
            for tool in tool_collection.tools
        ]
    )
    console.print(Panel(tool_info, title="Available Tools"))

    agent =  CodeAgent(
        tools=[DuckDuckGoSearchTool(), *tool_collection.tools], model=model
    )


def main():
    query = prompt(">>")
    console.print(f"[italic]Processing: {query}[/]")
    agent.run(query)

if __name__ == "__main__":
    main()

