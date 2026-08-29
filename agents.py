from tools import *
from states import FinancialData
from prompts import *
from langchain.agents import create_agent
from rich import print 
from langchain_core.globals import set_verbose, set_debug
from rich import print
from langgraph.graph import StateGraph
from langgraph.constants import END
from dotenv import load_dotenv
import os
from langchain_mistralai import ChatMistralAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm1 = ChatMistralAI(
    model = "mistral-small-latest",
    api_key=os.getenv("MISTRA_AI_API_KEY"),
    temperature=0
)

llm2 = ChatGoogleGenerativeAI(
    model = "gemini-3.1-flash-lite",
    api_key = os.getenv("GEMINI_API_KEY "),
    temperature = 0
)

def Doc_extractor():
    return create_agent(
        model=llm1,
        tools=[
            file_type_detector,
            pdf_extractor
        ],
        system_prompt= Extractor_prompt(),
        response_format=("structured", FinancialData)
    )
