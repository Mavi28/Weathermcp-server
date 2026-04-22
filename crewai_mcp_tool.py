from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters

load_dotenv()

#initiate llm provider/model
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0
)

server_params = StdioServerParameters(
    command = "C:\\Users\\90552\\anaconda3\\python.exe",
    args=[
        "C:\\Users\\90552\\OneDrive - Nişantaşı Üniversitesi -Öğrenci Mail Paneli\\Desktop\\mcp\\build_mcp_server\\weather.py",
        "run",
        "weather.py"
    ]
)

def get_weather_update(city):
    with MCPServerAdapter(server_params) as tools:
        print(f"Available tools from STDIO MCP Server: {[tool.name for tool in tools]}")

        weather_forecast_agent = Agent(
            role="Weather Forecast Analyst",
            goal="Provide a natural language weather update for any city requestes by the user, "
                 "incorporating all details from the tool output(e.g., weather condition and temperature).",
            backstory="You are a weather forecast assistant specializing in delivering quick and"
                      "accurate weather updates using live data, including both temperature and weather condition.",
            llm=llm,
            tools=tools,
            verbose=True,
        )

        weather_forecast_task = Task(
            description=(
                "Provide a natural language weather update for the city: {city}."
                "Incorporate all details from the tool output, such as weather condition and temperature, in a complete sentence."
            ),
            expected_output="A natural language sentence summarizing the weather condtion and temperature, for the requested city.",
            agent=weather_forecast_agent
        )

        weather_forecast_crew = Crew(
            agents=[weather_forecast_agent],
            tasks=[weather_forecast_task],
            verbose=True,
        )

        result = weather_forecast_crew.kickoff(inputs={"city": city})

        return result

if __name__ == "__main__":
    city = "Chennai"
    weather_forecast = get_weather_update(city)
    print(weather_forecast)