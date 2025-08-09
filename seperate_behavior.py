from agents import Agent,Runner,function_tool
from config import config
from agents.agent import StopAtTools
import asyncio

@function_tool
def subtract (a:int ,b:int)->int:
    """ Subtract two numbers"""
    print("Subtract called")
    return a-b+5
@function_tool
def human_review():
    "Human is the loop interface"
    print("Human review called")
    return ("Human in the loop called")

stop_at_tool_agent=Agent(
    name="Mustafa",
    instructions="You are ahelpful assisstant who stop on human review",
    tools=[subtract,human_review],
    tool_use_behavior=StopAtTools(stop_at_tool_names=["human_review"]) 
)

stop_on_first_tool_agent=Agent(
    name="Ali",
    instructions="you are a helpful assisstant who stops on first tool ",
    tools=[subtract,human_review],
    tool_use_behavior="stop_on_first_tool"
    
)

async def main():
    print("➡ Step 1: Subtraction")
    step1 = await Runner.run(stop_at_tool_agent, input="subtract 8 from 5", run_config=config)
    print("Output of step 1:", step1.final_output)

    print("➡ Step 2: Human Review")
    step2 = await Runner.run(stop_on_first_tool_agent, 
                             input="ask human to review ",
                             run_config=config)
    print("Output of step 2:", step2.final_output)
    
if __name__ == "__main__":
    asyncio.run(main())
