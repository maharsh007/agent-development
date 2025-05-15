# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Planning agent. A pre-booking agent covering the planning part of the trip."""

from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.genai.types import GenerateContentConfig
from .shared_libraries import types,constants
from .shared_libraries.constants import MODEL_GEMINI_2_0_FLASH
from .tools.memory import memorize
from .tools.memory import _load_precreated_itinerary
from .sub_agents.booking.agent import booking_agent
from .sub_agents.inspiration.agent import inspiration_agent
from .sub_agents.pre_trip.agent import pre_trip_agent
from .sub_agents.in_trip.agent import in_trip_agent
from .sub_agents.planning.agent import planning_agent
from .sub_agents.post_trip.agent import post_trip_agent



from . import prompt

root_agent = Agent(
    model=MODEL_GEMINI_2_0_FLASH,
    name="root_agent",
    description="A Travel Conceirge using the services of multiple sub-agents",
    instruction=prompt.ROOT_AGENT_INSTR,
    sub_agents=[
        inspiration_agent,
        planning_agent,
        booking_agent,
        pre_trip_agent,
        in_trip_agent,
        post_trip_agent,
    ],
    before_agent_callback=_load_precreated_itinerary,
)