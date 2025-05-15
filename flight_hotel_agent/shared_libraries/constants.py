"""Constants used as keys into ADK's session state."""

SYSTEM_TIME = "_time"
ITIN_INITIALIZED = "_itin_initialized"

ITIN_KEY = "itinerary"
PROF_KEY = "user_profile"

ITIN_START_DATE = "itinerary_start_date"
ITIN_END_DATE = "itinerary_end_date"
ITIN_DATETIME = "itinerary_datetime"

START_DATE = "start_date"
END_DATE = "end_date"

# --- Define Model Constants for easier use ---

MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash-001"

# Note: Specific model names might change. Refer to LiteLLM/Provider documentation.
MODEL_GPT_4O = "openai/gpt-4o"
MODEL_CLAUDE_SONNET = "anthropic/claude-3-5-sonnet-20240620"