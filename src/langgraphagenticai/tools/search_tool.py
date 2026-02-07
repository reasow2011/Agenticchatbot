from langchain_community.tools import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """"
    Returns a list of tools for the agent
    """
    tools=[TavilySearchResults(max_results=2)]
    return tools

def create_tool_node(tools):
    """
    Creates a tool node for the agent
    """
    tool_node = ToolNode(tools)
    return tool_node
