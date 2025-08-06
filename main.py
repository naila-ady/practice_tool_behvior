from config import config
from agents import Agent,Runner,function_tool
from agents.agent import StopAtTools

import asyncio

@function_tool
def add(a:int ,b:int)->int:
    """Add two numbers"""
    print("Add tool called")
    return a+b-5

@function_tool
def human_review():
    """Human is the loop interface"""
    print("Human review called")
    return "Human in the loop called"


Simple_agent=Agent(
    name="naila",
    instructions="You are a helpful asssistant",
    tools=[add,human_review],
    tool_use_behavior=StopAtTools(stop_at_tool_names=["human_review"])
)
async def main():
    result=await Runner.run(Simple_agent,input="2 main 2 plus krdo ,and afer addition ask human to review",run_config=config)
    print(result.final_output) 

if __name__=="__main__":
    asyncio.run(main())