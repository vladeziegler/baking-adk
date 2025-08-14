import os

from google.adk.agents import Agent
from .prompt import REMOTE_A2A_AGENT_PROMPT

class RemoteA2AAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "A2A Remote Agent"
        self.description = "This agent is responsible for handling all requests that require remote access to the A2A API."
        self.prompt = REMOTE_A2A_AGENT_PROMPT
        self.agent_card=f"http://localhost:8001/{os.environ.get('AGENT_CARD_WELL_KNOWN_PATH')}"

remote_a2a_agent = RemoteA2AAgent(
    name="sub_agent",
    model="gemini-2.5-pro",
    description="Helpful assistant that can conect to remote agents",
    instruction=REMOTE_A2A_AGENT_PROMPT,
)

