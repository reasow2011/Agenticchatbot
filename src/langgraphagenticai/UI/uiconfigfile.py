class Config:
    def __init__(self):
        pass

    def page_title(self):
        return "LangGraph Build Stateful Agentic AI graph"

    def page_icon(self):
        return "🚀"

    def get_llm_options(self):
        # This fixes the 'get_llm_options' error
        return ["Groq", "OpenAI", "Anthropic"]

    def get_usecase_options(self):
        return ["Basic Chatbot", "Chatbot with web search"]

    def get_model_options(self):
        # Default/Fallback models
        return ["gpt-4o", "claude-3-5-sonnet"]

    def groq_model_options(self):
        # Specific models for Groq
        return [
            "llama-3.3-70b-versatile", 
            "llama-3.1-8b-instant", 
            "mixtral-8x7b-32768"
        ]