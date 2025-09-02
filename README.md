# News Summarizer - Multi Agent
Fetch top 5 current global news topics
**Quick start**
This project demonstrates a minimal multi‑agent workflow using CrewAI with Google’s Gemini models and Firecrawl for web research. It configures Gemini via environment variables, defines two agents (Researcher and Summarizer), and runs sequential tasks to fetch and summarize top global news.

**Project structure**
main.py: Initializes Gemini client, defines CrewAI agents and tasks, wires Firecrawl as a tool, and runs the crew.

**Prerequisites**
Python 3.9+ recommended.

**Accounts and API keys:**

Gemini API key from Google AI Studio. Set as GEMINI_API_KEY.

Firecrawl API key from Firecrawl. Set as FIRECRAWL_API_KEY.

Internet access to call external APIs.

**Installation**
Clone the repository locally.

Create and activate a virtual environment.

**Install dependencies:**

pip install google-generativeai crewai "crewai[tools]" firecrawl-py python-dotenv

Optionally pin versions in requirements.txt for reproducibility.

Example:

python -m venv .venv && source .venv/bin/activate # Windows: .venv\Scripts\activate

pip install google-generativeai crewai "crewai[tools]" firecrawl-py python-dotenv

echo -e "GEMINI_API_KEY=\nFIRECRAWL_API_KEY=" > .env # then edit with real keys

**Environment variables**
GEMINI_API_KEY: Required. Used by google-generativeai and CrewAI’s Gemini-backed LLM.

FIRECRAWL_API_KEY: Required for FirecrawlSearchTool.


**Shell export:**

macOS/Linux: export GEMINI_API_KEY=...; export FIRECRAWL_API_KEY=...

Windows (Powershell): setx GEMINI_API_KEY "..." ; setx FIRECRAWL_API_KEY "..."

**Sequential tasks:** Task 1 asks the Researcher to fetch top global news; Task 2 asks the Summarizer to write one‑line summaries, leveraging CrewAI’s sequential process to pass context automatically.

