from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo


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

multimodel_agent = Agent(
    team=[websearch_agent, financial_agent],
    instructions=["Always include sources and dates in your search results", "Use table to display data in a clear and concise manner"],
    show_tool_calls=True,
    markdown=False
)

multimodel_agent.print_response("Summarize analyst recommendations and share the latest news for NVDA.",stream=True)
