"""Planning agent. A pre-booking agent covering the planning part of the trip."""

from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.genai.types import GenerateContentConfig
from ...shared_libraries import types, constants
from ...shared_libraries.constants import MODEL_GEMINI_2_0_FLASH
from ...tools.memory import memorize

from . import prompt

itinerary_agent = Agent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="itinerary_agent",
    description="Create and persist a structured JSON representation of the itinerary.",
    instruction=prompt.ITINERARY_AGENT_INSTR,
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
    output_schema=types.Itinerary,
    output_key="itinerary",
    generate_content_config=types.json_response_config,
)

hotel_room_selection_agent = Agent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="hotel_room_selection_agent",
    description="Help users with the room choices for a hotel",
    instruction=prompt.HOTEL_ROOM_SELECTION_INSTR,
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
    output_schema=types.RoomsSelection,
    output_key="room",
    generate_content_config=types.json_response_config,
)

hotel_search_agent = Agent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="hotel_search_agent",
    description="Help users find hotel around a specific geographic area",
    instruction=prompt.HOTEL_SEARCH_INSTR,
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
    output_schema=types.HotelsSelection,
    output_key="hotel",
    generate_content_config=types.json_response_config,
)


flight_seat_selection_agent = Agent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="flight_seat_selection_agent",
    description="Help users with the seat choices",
    instruction=prompt.FLIGHT_SEAT_SELECTION_INSTR,
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
    output_schema=types.SeatsSelection,
    output_key="seat",
    generate_content_config=types.json_response_config,
)

flight_search_agent = Agent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="flight_search_agent",
    description="Help users find best flight deals",
    instruction=prompt.FLIGHT_SEARCH_INSTR,
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
    output_schema=types.FlightsSelection,
    output_key="flight",
    generate_content_config=types.json_response_config,
)


planning_agent = Agent(
    model=MODEL_GEMINI_2_0_FLASH,
    description="""Helps users with travel planning, complete a full itinerary for their vacation, finding best deals for flights and hotels.""",
    name="planning_agent",
    instruction=prompt.PLANNING_AGENT_INSTR,
    tools=[
        AgentTool(agent=flight_search_agent),
        AgentTool(agent=flight_seat_selection_agent),
        AgentTool(agent=hotel_search_agent),
        AgentTool(agent=hotel_room_selection_agent),
        AgentTool(agent=itinerary_agent),
        memorize,
    ],
    generate_content_config=GenerateContentConfig(
        temperature=0.1, top_p=0.5
    )
)