from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

import phi
import os
from dotenv import load_dotenv
from phi.playground import Playground,serve_playground_app

load_dotenv()

phi.api_key = os.getenv("PHI_API_KEY")

websearch_agent = Agent(
    name='websearch_agent', 
    role='Search the web for financial information',
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources and dates in your search results"],
    show_tool_calls=True,
    markdown=False
)

financial_agent = Agent(
    name='Financial AI Analyst', 
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(
        stock_price=True,analyst_recommendations=True,stock_fundamentals=True,company_news=True
    )],
    instructions=["Use table to display data in a clear and concise manner"],
    show_tool_calls=True,
    markdown=False
)


app = Playground(agents=[websearch_agent,financial_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True)