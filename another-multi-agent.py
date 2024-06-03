import os
from typing import Optional, List

import streamlit as st
from dotenv import load_dotenv
from langchain_experimental.tools import PythonREPLTool
from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from phi.tools.hackernews import HackerNews

# Definir la herramienta PythonREPLTool

load_dotenv()

openai_api_key = st.text_input(
    "OpenAI api key: ", type="password", value=os.getenv("OPENAI_API_KEY")
)

st.title("Hacker News Assistant")
st.caption(
    "Ask Hacker News questions and get the answers. You can also ask for python code."
)

if openai_api_key:
    # Create instances of the Assistant
    story_researcher = Assistant(
        name="HackerNews Story Researcher",
        role="Researches hackernews stories and users.",
        tools=[HackerNews()],
        llm=OpenAIChat(
            model="gpt-4o", max_tokens=1024, temperature=0.5, api_key=openai_api_key
        ),
    )

    user_researcher = Assistant(
        name="HackerNews User Researcher",
        role="Reads articles from URLs.",
        tools=[HackerNews()],
        llm=OpenAIChat(
            model="gpt-4o", max_tokens=1024, temperature=0.5, api_key=openai_api_key
        ),
    )

    # Asistente de Desarrollo
    dev_assistant = Assistant(
        name="Development Assistant",
        role="Helps with coding and development tasks",
        tools=[HackerNews(), PythonREPLTool()],
        llm=OpenAIChat(
            model="gpt-4o", max_tokens=1024, temperature=0.5, api_key=openai_api_key
        ),
    )

    myteam: Optional[List["Assistant"]] = [
        story_researcher,
        user_researcher,
        dev_assistant,
    ]

    hn_assistant = Assistant(
        name="Hackernews Team",
        role="Researches hackernews stories and users.",
        team=myteam,
        llm=OpenAIChat(
            model="gpt-4o", max_tokens=1024, temperature=0.5, api_key=openai_api_key
        ),
    )
    query = st.text_input("Ask Hacker News")

    if query:
        response = hn_assistant.run(query, stream=False)
        st.write(response)
        # Run the PythonREPLTool with the query
        response = hn_assistant.run(query, stream=False, tools=[PythonREPLTool()])
        st.write(response)
