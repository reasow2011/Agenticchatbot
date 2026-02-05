from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.Nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.State.state import State

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)
        self.basic_chatbot_node = BasicChatbotNode(self.llm)

    def basic_chatbot_build_graph(self):
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def setup_graph(self, usecase: str):
        # FIX 1: Check for "Chatbot" (what your UI sends), not "Basic Chatbot"
        if usecase == "Chatbot" or usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        
        # FIX 2: Always return the compiled graph
        return self.graph_builder.compile()