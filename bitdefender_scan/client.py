import asyncio
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

client = MultiServerMCPClient(
    {
        "Server": {
            "url": "http://localhost:8000/mcp",
            "transport": "streamable_http",
        },
    }
)
tools = asyncio.run(client.get_tools())

graph = create_react_agent(
    ChatOllama(model="mistral:7b", temperature=0.5, num_predict=-1),
    tools
)
