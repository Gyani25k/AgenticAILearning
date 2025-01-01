# Financial AI Analyst (FIA)

## Overview
Financial AI Analyst (FIA) is a multimodal AI financial agent designed to assist with financial analysis by leveraging web search capabilities and the `yfinance` tool. Additionally, a playground is included for users to interact and experiment with the agent.

---

## Features
- **AI-Powered Financial Analysis:** Utilize the agent for real-time financial data retrieval and analysis.
- **Web Search Integration:** Enhance insights with supplementary data from the web.
- **`yfinance` Integration:** Access and analyze financial market data with ease.
- **Interactive Playground:** Experiment and interact with the AI agent in a user-friendly environment.

---

## Installation Guide

### Prerequisites
1. Ensure Python is installed on your system. (Recommended: Python 3.8+)
2. Install `venv` for creating a virtual environment.

---

### Steps to Set Up

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Gyani25k/AgenticAILearning.git
   cd Financial-AI-Analyst
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   - Create a `.env` file in the project directory.
   - Add the necessary environment variables (API keys, configurations, etc.) required for web search and `yfinance`.

5. **Run the Agent**
   ```bash
   python financial_agent.py
   ```

6. **Run the Playground**
   ```bash
   python playground.py
   ```

---

## Usage

1. **Financial Agent**
   - Execute `financial_agent.py` to use the financial AI agent for analysis and insights.

2. **Playground**
   - Run `playground.py` for an interactive experience with the AI agent. This is ideal for testing and experimenting with its capabilities.

---
