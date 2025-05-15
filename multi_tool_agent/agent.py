from google.adk.agents import Agent
from .sub_agent import greeting_agent, farewell_agent, llm_option
from .prompts import GLOBAL_INSTRUCTION, INSTRUCTION
from .tools.search import google_search_grounding


from .shared_libraries.callbacks import (
    rate_limit_callback,
    before_agent,
    before_tool,
)
from .tools.tools import (
    send_call_companion_link,
    approve_discount,
    sync_ask_for_approval,
    update_salesforce_crm,
    access_cart_information,
    modify_cart,
    get_product_recommendations,
    check_product_availability,
    schedule_planting_service,
    get_available_planting_times,
    send_care_instructions,
    generate_qr_code,
)
from google.adk.runners import Runner
from .helper import APP_NAME
from .session import session_service_stateful # Ensure session service is imported

# @title Define the Root Agent with Sub-Agents

# Ensure sub-agents were created successfully before defining the root agent.
# Also ensure the original 'get_weather' tool is defined.
root_agent = None
runner_root_stateful = None # Initialize runner


    # Let's use a capable Gemini model for the root agent to handle orchestration
root_agent_model = llm_option


root_agent = Agent(
    name="Customer_agent", # Give it a new version name
    model=root_agent_model,
    global_instruction=GLOBAL_INSTRUCTION,
    instruction=INSTRUCTION,
    tools=[
        send_call_companion_link,
        approve_discount,
        sync_ask_for_approval,
        update_salesforce_crm,
        access_cart_information,
        modify_cart,
        get_product_recommendations,
        check_product_availability,
        schedule_planting_service,
        get_available_planting_times,
        send_care_instructions,
        generate_qr_code,
        google_search_grounding
    ], # Root agent still needs the weather tool for its core task
    # Key change: Link the sub-agents here!
    sub_agents=[greeting_agent, farewell_agent],
    before_tool_callback=before_tool,
    before_agent_callback=before_agent,
    before_model_callback=rate_limit_callback,
)
print(f"✅ Root Agent '{root_agent.name}' created using model '{root_agent_model}' with sub-agents: {[sa.name for sa in root_agent.sub_agents]}")

runner_root_stateful = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=session_service_stateful # Use the NEW stateful session service
)
print(f"✅ Runner created for stateful root agent '{runner_root_stateful.agent.name}' using stateful session service.")

# root_agent = Agent(
#     name="weather_time_agent",
#     model="gemini-2.0-flash",
#     description=(
#         "Agent to answer questions about the time and weather in a city."
#     ),
#     instruction=(
#         "You are a helpful agent who can answer user questions about the time and weather in a city."
#     ),
#     tools=[get_weather, get_current_time],
# )