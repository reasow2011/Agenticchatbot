# 🤖 Agentic AI Chatbot

An end-to-end agentic AI chatbot built with LangGraph, LangChain, and Streamlit. This project implements a sophisticated conversational AI system that uses agentic workflows for intelligent task handling and response generation.

## 📋 Overview

This chatbot leverages the power of LangGraph to create stateful, multi-step conversational agents that can reason, plan, and execute complex tasks. It provides a user-friendly web interface built with Streamlit for seamless interaction.

## ✨ Features

- **Agentic Architecture**: Built on LangGraph for sophisticated agent-based workflows
- **Multi-LLM Support**: Integration with multiple language model providers:
  - OpenAI
  - Google Gemini (GenAI and Vertex AI)
  - Groq
- **Interactive Web Interface**: Streamlit-based UI for easy interaction
- **Modular Design**: Clean, maintainable code structure with separation of concerns

## 🛠️ Tech Stack

- **LangChain**: Core framework for LLM application development
- **LangGraph**: State machine orchestration for agentic workflows
- **Streamlit**: Web interface framework
- **Python**: Primary programming language
- **Multiple LLM Providers**: OpenAI, Google AI, Groq

## 📁 Project Structure

```
Agenticchatbot/
├── src/
│   └── langgraphagenticai/
│       └── main.py              # Main application logic
├── app.py                        # Application entry point
├── requirements.txt              # Python dependencies
├── .gitignore                    # Git ignore rules
└── README.md                     # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- API keys for your chosen LLM provider(s):
  - OpenAI API key
  - Google AI API key (for Gemini)
  - Groq API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/reasow2011/Agenticchatbot.git
   cd Agenticchatbot
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory and add your API keys:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   GOOGLE_API_KEY=your_google_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   ```

### Running the Application

Start the application by running:

```bash
python app.py
```

This will launch the Streamlit web interface, typically accessible at `http://localhost:8501`

## 📦 Dependencies

```
langchain                    # LangChain core framework
langchain_community          # Community integrations
langchain_core              # Core abstractions
langchain_openai            # OpenAI integration
langchain_groq              # Groq integration
langchain_google_genai      # Google Gemini integration
langchain_google_vertexai   # Google Vertex AI integration
langgraph                   # State machine for agents
python-dotenv               # Environment variable management
streamlit                   # Web interface
protobuf                    # Protocol buffers
grpcio                      # gRPC support
```

## 🎯 Usage

1. Launch the application using `python app.py`
2. Open your web browser to the provided Streamlit URL
3. Start conversing with the chatbot
4. The agent will process your requests using its agentic workflow capabilities

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🔗 Links

- **Repository**: [https://github.com/reasow2011/Agenticchatbot](https://github.com/reasow2011/Agenticchatbot)
- **LangChain Documentation**: [https://python.langchain.com/](https://python.langchain.com/)
- **LangGraph Documentation**: [https://langchain-ai.github.io/langgraph/](https://langchain-ai.github.io/langgraph/)
- **Streamlit Documentation**: [https://docs.streamlit.io/](https://docs.streamlit.io/)

## 📧 Contact

For questions, issues, or suggestions, please open an issue on GitHub.

---

**Built with ❤️ using LangGraph and LangChain**