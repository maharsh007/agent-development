# Multi Tool Agent

This project demonstrates a simple multi-tool agent built using the Google Agent Development Kit (ADK). The agent can answer questions about the current weather and time in a specified city.

## Features

- **Weather Report**: Retrieve the current weather for supported cities.
- **Current Time**: Get the current time for supported cities.

Currently, only "New York" is supported for both weather and time queries.

## Requirements

- Python 3.9+
- [Google Agent Development Kit (ADK)](https://github.com/google/agent-development-kit)
- `zoneinfo` (included in Python 3.9+)

## Installation

1. Clone this repository:
    ```bash
    git clone <repository-url>
    cd multi_tool_agent
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

The main agent is defined in `agent.py`. It provides two tools:
- `get_weather(city: str)`: Returns the weather report for the specified city.
- `get_current_time(city: str)`: Returns the current time for the specified city.

Example usage:
```python
from agent import root_agent

result = root_agent.tools[0]("New York")  # get_weather
print(result)

result = root_agent.tools[1]("New York")  # get_current_time
print(result)