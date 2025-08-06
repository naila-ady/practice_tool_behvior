from agents import Agent,OpenAIChatCompletionsModel,AsyncOpenAI
from agents.run import RunConfig
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())
import os


gemini_api_key=os.getenv("GEMINI_API_KEY")

client=AsyncOpenAI(
    api_key= gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"    
)

model=OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
    
)
config=RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)

