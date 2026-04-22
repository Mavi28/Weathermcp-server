import streamlit as st

st.set_page_config(page_title="MCP Server", page_icon="⚙️")

st.title("⚙️ MCP Weather Server")
st.markdown("---")

st.markdown("""
A **Model Context Protocol (MCP) server** that exposes weather tools 
to AI agents through a standardised interface.
""")

col1, col2, col3 = st.columns(3)
col1.metric("Protocol", "MCP")
col2.metric("Transport", "SSE")
col3.metric("Status", "Live")

st.markdown("---")
st.subheader("🛠️ Available Tools")

with st.expander("get_weather(city)"):
    st.write("Returns current weather data for a given city.")

with st.expander("get_forecast(city, days)"):
    st.write("Returns a multi-day weather forecast.")

st.markdown("---")
st.subheader("🔧 Tech Stack")
st.code("Python · FastAPI · MCP SDK · uvicorn · SSE", language="bash")

st.info("This MCP server is designed to be connected to AI agents and LLM pipelines, not used directly in a browser.")