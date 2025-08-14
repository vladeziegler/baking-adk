from google.adk.agents import Agent
from .prompt import CALCULATOR_AGENT_PROMPT
from google.adk.agents import Agent


sub_agent = Agent(
    name="sub_agent",
    model="gemini-2.0-flash",
    description="",
    instruction=SUB_AGENT_PROMPT
) 