from src.langgraphagenticai.State.state import State

class ChatbotwithToolNode:

    #Chatbot enhanced with tool integratio
    def __init__(self, model):
        self.llm = model

    def process(self, state):
        """Process and input and generates a response with tool integration"""

        user_input=state['messages'][-1] if state['messages'] else ""
        llm_response=self.llm.invoke([{"role":"user","content":user_input}])

        #Stimulate tool specfic logic
        tools_response=f"Tool integration for: {user_input}"
        return {"messages": [llm_response, tools_response]}
    
    def create_chatbot(self,tools):
        llm_with_tools=self.llm.bind_tools(tools)
        
        def chatbot_node(state):
            return{"messages":llm_with_tools.invoke(state['messages'])}
        
        return chatbot_node
            