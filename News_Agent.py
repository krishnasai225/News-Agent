import os
import google.generativeai as genai

# Set your Gemini API key as an environment variable
api_key = os.getenv("GEMINI_API_KEY")
firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash")

response = model.generate_content("Hello, how are you?")

#print(response.text)

from crewai import Agent, Task, Crew, LLM

agent = Agent(
  role = "Motivational Speaker",
  goal = "Create an inspirational LinkedIn post for job seekers",
  backstory = "An experienced career mentor who inspires others through writing.",
  llm = LLM(model="gemini/gemini-2.0-flash",api_key=api_key)
)

from crewai import Agent, Task, Crew, LLM
from crewai_tools import FirecrawlSearchTool


search_tool = FirecrawlSearchTool(api_key=firecrawl_api_key)

# Agent 1: Researcher
researcher = Agent(
    role="Current Affairs Researcher",
    goal="Fetch top 5 current global news topics",
    backstory="An expert news researcher with access to latest information.",
    tools=[search_tool],
    llm=LLM(model="gemini/gemini-2.0-flash",api_key=api_key)
)

# Agent 2: Summarizer
summarizer = Agent(
    role="Note Maker",
    goal="Convert research into clear, short bullet points",
    backstory="An expert in simplifying complex topics for fast reading.",
    llm=LLM(model="gemini/gemini-2.0-flash",api_key=api_key)
)

# Tasks
task1 = Task(
    description="Search for the top 5 global news stories using the web.",
    expected_output = "Top 5 global news stories and its details",
    agent=researcher
)

task2 = Task(
    description="Take the news articles from previous task and write clear 1-line summaries for each.",
    expected_output = "Summarised and consumable notes",
    agent=summarizer
)

# Crew
current_affairs_crew = Crew(
    agents=[researcher, summarizer],
    tasks=[task1, task2],
    process="sequential"
)

print(current_affairs_crew.kickoff())