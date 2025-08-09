from config import config
from agents import Agent,Runner,function_tool,ModelSettings,enable_verbose_stdout_logging
from agents.agent import StopAtTools

import asyncio
# enable_verbose_stdout_logging()

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


stop_at_tool_agent=Agent(
    name="naila",
    instructions="You are a helpful asssistant who will stop at human_review tool ",
    tools=[human_review,add],
    # tool_use_behavior=StopAtTools(stop_at_tool_names=["human_review"]),
    handoff_description="Handles human_review tool  ",
)

on_first_tool_agent=Agent(
    name="Adnan",
    instructions="YOu are a helpful assisstant who stops on first tool used",
    tools=[add,human_review],
    # tool_use_behavior="stop_on_first_tool",
    handoff_description="Handles add tool"

)

triage_agent=Agent(
    name="triage_agent",
    instructions="You are a triage agent and transfer to agents as per the user input",
    tools=[add,human_review],
    # tool_use_behavior=StopAtTools(stop_at_tool_names=["add"]),
    tool_use_behavior=StopAtTools(stop_at_tool_names=["human_review"]),
    # agar ye line uncomment ki to handsoff srf human_review tool call
    # hoga aur sath m runner mai input m say add ko hata kr review akhri may dena hoga
    # tool_use_behavior="stop_on_first_tool", 
    handoffs=[on_first_tool_agent,stop_at_tool_agent]
)


async def main():
    result=await Runner.run(triage_agent,input=" aur 2 main 2 plus kro ,aur phir human review karo",run_config=config)
    print(result.final_output) 

if __name__=="__main__":
    asyncio.run(main())