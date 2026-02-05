import streamlit as st
from langchain_core.messages import HumanMessage

class DisplayResultsStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_results_on_ui(self):
        # 1. Display user message in chat history
        st.chat_message("user").write(self.user_message)
        
        # 2. Show a spinner while waiting for the LLM
        with st.spinner("Thinking..."):
            try:
                # 3. Create the initial state with the user's message
                initial_state = {"messages": [HumanMessage(content=self.user_message)]}
                
                # 4. Run the graph!
                response = self.graph.invoke(initial_state)
                
                # 5. Extract the last message (the AI's response)
                ai_response = response['messages'][-1].content
                
                # 6. Display AI response
                st.chat_message("assistant").write(ai_response)

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.write(e) # This helps debugging