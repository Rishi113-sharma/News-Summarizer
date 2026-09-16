from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from transformers import BitsAndBytesConfig
from langchain_core.output_parsers import StrOutputParser
from langchain_community.tools.tavily_search import TavilySearchResults 
search_tools = TavilySearchResults(max_results= 5)

import torch
import warnings
import logging


logging.getLogger("transformers").setLevel(logging.ERROR)

warnings.filterwarnings(
    "ignore",
    message=".*Both `max_new_tokens`.*and `max_length`.*"
)


quant_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True
)


llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    device_map="auto",
    model_kwargs={
        "quantization_config": quant_config
    },
    pipeline_kwargs={
        "max_new_tokens": 4096,
        "temperature": 0.7,
        "do_sample": True,
        "return_full_text": False,
        "clean_up_tokenization_spaces": False,
    },
)
model = ChatHuggingFace(llm=llm)
prompt= ChatPromptTemplate.from_template(
    """
    you are a helpful assitant 
    summarize the following news into clear bullet points
    {news}
    """
)
runnable = prompt | model | StrOutputParser()
def get_news(query):
    news_result = search_tools.run(query) 
    result = runnable.invoke({ 
                              "news": news_result 
                              }) 
    return result