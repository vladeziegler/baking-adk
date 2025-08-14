from google.adk.agents import Agent
from .prompt import ROOT_AGENT_PROMPT

root_agent = Agent(
    name="root_agent",
    model="gemini-2.0-flash",
    description="",
    sub_agents=[],
    instruction=ROOT_AGENT_PROMPT
)