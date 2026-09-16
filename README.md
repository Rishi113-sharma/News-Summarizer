### News Summarizer

Developed a **Generative AI-powered News Summarizer** that retrieves the latest news on a user-provided topic using **Tavily Search** and generates concise, easy-to-understand bullet-point summaries using the **Qwen2.5-7B-Instruct** language model.

The project is separated into two components. **`base.py`** contains the core AI pipeline, including Tavily news retrieval, the Qwen local LLM, LangChain prompt processing, and output parsing. **`app.py`** provides the **Streamlit user interface**, allowing users to enter a news topic and view the generated summary.

The Qwen model is optimized using **4-bit NF4 quantization** and runs locally with GPU acceleration, enabling efficient inference on an NVIDIA RTX 3060. API credentials are managed securely using environment variables.

### Technologies Used

**Python • Generative AI • Qwen2.5-7B-Instruct • LangChain • Streamlit • Hugging Face Transformers • Tavily Search • PyTorch • CUDA • BitsAndBytes • 4-bit NF4 Quantization • Prompt Engineering • Output Parsing • Environment Variables**

### Project Structure

```text
News-Summarizer/
│
├── base.py    # LLM, Tavily search & summarization pipeline
├── app.py     # Streamlit frontend
├── .env       # API keys 
└── .gitignore
```

### Workflow

**User enters topic → Tavily retrieves news → LangChain prompt → Qwen2.5-7B summarizes → Streamlit displays summary**

