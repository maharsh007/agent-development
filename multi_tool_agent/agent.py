from google.adk.agents import Agent
from .sub_agent import greeting_agent, farewell_agent, llm_option
from .tools import get_weather_stateful,get_current_time
from google.adk.runners import Runner
from .helper import APP_NAME
from .session import session_service_stateful # Ensure session service is imported
from .guardrail import block_keyword_guardrail,block_paris_tool_guardrail # Ensure guardrail is imported

# @title Define the Root Agent with Sub-Agents

# Ensure sub-agents were created successfully before defining the root agent.
# Also ensure the original 'get_weather' tool is defined.
root_agent = None
runner_root_stateful = None # Initialize runner

if greeting_agent and farewell_agent and 'get_weather' and 'get_current_time' in globals():
    # Let's use a capable Gemini model for the root agent to handle orchestration
    root_agent_model = llm_option

    root_agent = Agent(
        name="weather_agent_v2", # Give it a new version name
        model=root_agent_model,
        description="The main coordinator agent. Handles weather requests and delegates greetings/farewells to specialists.",
        instruction="You are the main Weather Agent coordinating a team. Your primary responsibility is to provide weather information. "
                    "Use the 'get_weather_stateful' tool ONLY for specific weather requests (e.g., 'weather in London'). "
                    "The tool will format the temperature based on user preference stored in state."
                    "Use the 'get_time' tool ONLY for specific time requests (e.g., 'time in London'). "
                    "You have specialized sub-agents: "
                    "1. 'greeting_agent': Handles simple greetings like 'Hi', 'Hello'. Delegate to it for these. "
                    "2. 'farewell_agent': Handles simple farewells like 'Bye', 'See you'. Delegate to it for these. Exit the chat after farewell. "
                    "Analyze the user's query. If it's a greeting, delegate to 'greeting_agent'. If it's a farewell, delegate to 'farewell_agent'. "
                    "If it's a weather request, handle it yourself using 'get_weather_stateful'. "
                    "For anything else, respond appropriately or state you cannot handle it.",
        tools=[get_weather_stateful,get_current_time], # Root agent still needs the weather tool for its core task
        # Key change: Link the sub-agents here!
        sub_agents=[greeting_agent, farewell_agent],
        output_key="last_weather_report",
        before_model_callback=block_keyword_guardrail,
        before_tool_callback=block_paris_tool_guardrail
    )
    print(f"✅ Root Agent '{root_agent.name}' created using model '{root_agent_model}' with sub-agents: {[sa.name for sa in root_agent.sub_agents]}")

    runner_root_stateful = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service_stateful # Use the NEW stateful session service
    )
    print(f"✅ Runner created for stateful root agent '{runner_root_stateful.agent.name}' using stateful session service.")

else:
    print("❌ Cannot create root agent because one or more sub-agents failed to initialize or 'get_weather' tool is missing.")
    if not greeting_agent: print(" - Greeting Agent is missing.")
    if not farewell_agent: print(" - Farewell Agent is missing.")
    if 'get_weather' not in globals(): print(" - get_weather function is missing.")
    if 'get_current_time' not in globals(): print(" - get_current_time function is missing.")

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