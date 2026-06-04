# from langchain_ollama import OllamaLLM

# llm = OllamaLLM(
#     model="llama3",
#     temperature=0.2,
# )

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os 
load_dotenv()  
api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=api_key,
    temperature=0.7,
)