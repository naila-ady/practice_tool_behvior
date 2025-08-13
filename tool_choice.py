from agents import Agent,Runner,ModelSettings,function_tool
from config import config
import asyncio
from agents import enable_verbose_stdout_logging

# enable_verbose_stdout_logging()

@function_tool
def add(a:int|str,b:int)->int:
    print("add tool called")
    return a+b-5

@function_tool
def checker():
    print("check tool is called")
    return "check in the loop called"

agent=Agent(
    name="simple Agent",
    instructions="you are as simple agent and do nothing special",
    tools=[add,checker],
    model_settings=ModelSettings(tool_choice="required"),
    reset_tool_choice=False
)

# print(agent.tools)
async def main():
    result=await Runner.run(agent,input=" give sum of 2 and 2",run_config=config,max_turns=10)
    print(result.final_output)
    
if __name__ == "__main__":
    asyncio.run(main())


    
