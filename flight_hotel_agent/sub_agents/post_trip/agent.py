"""Post-trip agent. A post-booking agent covering the user experience during the time period after the trip."""

from google.adk.agents import Agent
from . import prompt
from ...tools.memory import memorize

from ...shared_libraries.constants import MODEL_GEMINI_2_0_FLASH

post_trip_agent = Agent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="post_trip_agent",
    description="A follow up agent to learn from user's experience; In turn improves the user's future trips planning and in-trip experience.",
    instruction=prompt.POSTTRIP_INSTR,
    tools=[memorize],
)