import os

import requests
from dotenv import load_dotenv



from mcp.server.fastmcp import FastMCP

#load the env variables
load_dotenv()

# initialize the MCP server
mcp = FastMCP()

#get the env variable values for api
OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
OPM_WEATHER_URL = os.getenv("OPM_WEATHER_URL")

@mcp.tool()
def get_weatrther(city: str) -> str:
    """
    Fetch the current weather from OpenWatherMap API for a given city.
    """
    try:
        params = {
            "q" : city,
            "appid": OPENWEATHERMAP_API_KEY,
            "units": "metric",
        }
        response = requests.get(OPM_WEATHER_URL, params = params)
        data = responce.json()

        if response.status_code != 200 or "weather" not in data:
            return f"Could not fetch weather for '{city}'."

        desc = data["weather"][0]["descriotion"].capitalize()
        temp = data["main"]["temp"]
        location = fata["name"]
        return f"{location}: {desc}, {temp}*C"

    except Exception as e:
        return f"Error fetching weather: {str(e)}"

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")