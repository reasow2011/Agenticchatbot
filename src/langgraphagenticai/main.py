import streamlit as st
from src.langgraphagenticai.UI.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMs.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.UI.streamlitui.displayresults import DisplayResultsStreamlit


def load_langraph_agentic_ai_app():
    """
    Loads and runs the langraph agentic ai app with Streamlit UI.
    Initializes UI, handles user inputs, and calls the LLM model.
    """
    # Initialize the UI class
    ui_manager = LoadStreamlitUI()
    
    # Load the sidebar/controls and get user settings
    user_input = ui_manager.load_streamlit_ui()
    
    if not user_input:
        st.error("Please provide the required inputs")
        return  # This works now because it is inside a 'def'
    
    # Chat interface
    user_message = st.chat_input("Enter your message")
    
    if user_message:
        try:
            ##configure LLM
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("LLM model not found")
                return
            
            #usecase selection
            usecase = user_input['usecase_option']

            if not usecase:
                st.error("Please select a usecase")
                return
            
            #graph builder
            graph_builder = GraphBuilder(model)
            try:
                graph=graph_builder.setup_graph(usecase)
                DisplayResultsStreamlit(usecase, graph, user_message).display_results_on_ui()

            except Exception as e:
                st.error(f"Error in setting up graph: {str(e)}")
                return
        
        except Exception as e:
            st.error(f"Error in loading graph: {str(e)}")
            return
             

            
            