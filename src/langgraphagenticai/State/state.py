from typing import List, Annotated
from typing_extensions import TypedDict
from langchain_core.messages import BaseMessage
# FIX: Import add_messages from langgraph.graph
from langgraph.graph import add_messages

class State(TypedDict):
    """
    Represents the structure of the state of the graph
    """
    messages: Annotated[List[BaseMessage], add_messages]