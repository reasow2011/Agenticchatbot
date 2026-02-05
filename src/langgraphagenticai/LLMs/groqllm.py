import os
import streamlit as st
from langchain_groq import ChatGroq

# ERROR CAUSE: If there are ANY spaces before 'class', the import fails.
# Ensure 'class' is flush with the start of the line.
class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input
    
    def get_llm_model(self):
        try:
            # Use .get() to avoid key errors
            groq_api_key = self.user_controls_input.get('groq_api_key')
            selected_groq_model = self.user_controls_input.get('selected_groq_model')

            # Fallback to env var if empty
            if not groq_api_key:
                groq_api_key = os.getenv("GROQ_API_KEY")
            
            # Validation
            if not groq_api_key:
                st.error("Groq API Key is required")
                return None

            # Initialize Model
            llm = ChatGroq(model_name=selected_groq_model, api_key=groq_api_key) 
            return llm
    
        except Exception as e:
            raise ValueError(f"Error in getting LLM model: {str(e)}")