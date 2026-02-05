from langchain_core.messages import HumanMessage, SystemMessage

class BasicChatbotNode:
    def __init__(self, model):
        self.model = model

    def process(self, state):
        # 1. Get the messages from the state
        messages = state['messages']
        
        # 2. Invoke the LLM
        response = self.model.invoke(messages)
        
        # 3. Return the update (this appends to the state history)
        return {"messages": [response]}