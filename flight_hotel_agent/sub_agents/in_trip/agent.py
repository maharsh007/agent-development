"""In-trip agent. A post-booking agent covering the user experience during the trip."""

from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from ...shared_libraries.constants import MODEL_GEMINI_2_0_FLASH

from . import prompt

from .tools import (
    transit_coordination,
    flight_status_check,
    event_booking_check,
    weather_impact_check,
)

from ...tools.memory import memorize

day_of_agent = Agent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="day_of_agent",
    description="Day_of agent is the agent handling the travel logistics of a trip.",
    instruction=transit_coordination,
)

trip_monitor_agent = Agent(
    model="MODEL_GEMINI_2_0_FLASH",
    name="trip_monitor_agent",
    description="Monitor aspects of a itinerary and bring attention to items that necessitate changes",
    instruction=prompt.TRIP_MONITOR_INSTR,
    tools=[flight_status_check, event_booking_check, weather_impact_check],
    output_key="daily_checks",  # can be sent via email.
)

in_trip_agent = Agent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="in_trip_agent",
    description="Provide information about what the users need as part of the tour.",
    instruction=prompt.INTRIP_INSTR,
    sub_agents=[
        trip_monitor_agent
    ],  # This can be run as an AgentTool. Illustrate as an Agent for demo purpose.
    tools=[
        AgentTool(agent=day_of_agent), 
        memorize
    ],
)


