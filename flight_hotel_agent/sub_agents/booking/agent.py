"""Booking agent and sub-agents, handling the confirmation and payment of bookable events."""

from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.genai.types import GenerateContentConfig

from . import prompt


from ...shared_libraries.constants import MODEL_GEMINI_2_0_FLASH

create_reservation = Agent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="create_reservation",
    description="""Create a reservation for the seclected item.""",
    instruction=prompt.CONFIRM_RESERVATION_INSTR
)

payment_choice = Agent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="payment_choice",
    description="""Show the user the payment choices and ask the user for form of payment.""",
    instruction=prompt.PAYMENT_CHOICE_INSTR
)

process_payment = Agent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="process_payment",
    description="""Process the payment for the selected item.Completing the Transaction""",
    instruction=prompt.PROCESS_PAYMENT_INSTR
)

booking_agent = Agent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="booking_agent",
    description="Given an itinerary, complete the bookings of items by handling payment choices and processing.",
    instruction=prompt.BOOKING_AGENT_INSTR,
    tools =[
        AgentTool(agent=create_reservation),
        AgentTool(agent=payment_choice),
        AgentTool(agent=process_payment)
    ],
    generate_content_config=GenerateContentConfig(
        max_output_tokens=512,
        temperature=0.0,
        top_p=0.5,
        top_k=40,
        stop_sequences=["<end_of_text>"],
    )
)
