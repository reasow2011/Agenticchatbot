from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.Nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.State.state import State
from src.langgraphagenticai.tools.search_tool import get_tools, create_tool_node
from langgraph.prebuilt import tools_condition
from src.langgraphagenticai.Nodes.chatbot_with_tool_nodes import ChatbotwithToolNode

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)
        self.basic_chatbot_node = BasicChatbotNode(self.llm)

    def basic_chatbot_build_graph(self):
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
    
    def chatbot_with_tools_build_graph(self):
        #Define tool and tool nodes
        tools=get_tools()
        tool_node=create_tool_node(tools)

        #Define LLMs
        llm_node=self.llm
        

        #Define chatbot node
        obj_chatbot_with_node=ChatbotwithToolNode(llm)
        chatbot_node=obj_chatbot_with_node.create_chatbot(tools)
        
             #Add nodes
        self.graph_builder.add_node("chatbot",chatbot_node )
        self.graph_builder.add_node("tool", tool_node)

        #Define conditional and direct edges
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edge("chatbot",tools_condition)
        self.graph_builder.add_edge("tool","chatbot")
        self.graph_builder.add_edge("chatbot", END)
        
        

    def setup_graph(self, usecase: str):
        # FIX 1: Check for "Chatbot" (what your UI sends), not "Basic Chatbot"
        if usecase == "Chatbot with web search":
            self.chatbot_with_tools_build_graph()
        elif usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        
        # FIX 2: Always return the compiled graph
        return self.graph_builder.compile()