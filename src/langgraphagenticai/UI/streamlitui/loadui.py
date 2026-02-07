import streamlit as st
import os
from src.langgraphagenticai.UI.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}
    
    def load_streamlit_ui(self):
        st.set_page_config(page_title="LangGraph Agentic AI", layout="wide")
        st.header("LangGraph Build Stateful Agentic AI Graph")

        with st.sidebar:
            llm_option = self.config.get_llm_options()
            usecase_option = self.config.get_usecase_options()
            
            self.user_controls['llm_option'] = st.selectbox("LLM", llm_option)
            
            if self.user_controls['llm_option'] == 'Groq':
                model_option = self.config.groq_model_options()
                self.user_controls['selected_groq_model'] = st.selectbox("Model", model_option)
                
                # --- THIS IS THE MISSING PART ---
                # You must assign the text_input result to the dictionary key 'groq_api_key'
                self.user_controls['groq_api_key'] = st.text_input("Groq API Key", type="password")
                # --------------------------------
                
                if not self.user_controls['groq_api_key']:
                     st.info("Please enter your Groq API Key to continue.")

            self.user_controls['usecase_option'] = st.selectbox("Usecase", usecase_option)
            
            if self.user_controls['usecase_option'] == 'Chatbot with web search':
                os.environ["TAVILY_API_KEY"]=self.user_controls['TAVILY_API_KEY'] = st.session_state["TAVILY_API_KEY"]=st.text_input("TAVILY_API_KEY", type="password")

                               
                if not self.user_controls['TAVILY_API_KEY']:
                    st.info("Please enter your Tavily API Key to continue.")
        return self.user_controls