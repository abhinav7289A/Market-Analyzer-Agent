# Multi‑Agent Market Research System

A modular, multi‑agent pipeline that automates end‑to‑end market research for any topic. It combines specialized AI agents for data gathering, analysis, and report writing—wrapped in an interactive Streamlit UI.

---
## Installation

bash
#### Clone and enter repo
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

#### Create & activate virtual environment
python -m venv venv
#### Windows:
venv\Scripts\activate
#### macOS/Linux:
source venv/bin/activate

#### Install dependencies
pip install -r requirements.txt

## Overview

Modern market research demands both speed and depth: automated agents can scour the web, extract insights, and generate polished reports in minutes. This system comprises three core components:

1. **Research Agent**  
   - Uses SerpAPI (Google Search Results API) to retrieve the top 5 relevant articles, links, and snippets for a given topic.  
   - Outputs a list of `{ title, link, snippet }` objects as raw data.

2. **Analysis Agent**  
   - Leverages LLMs (OpenAI’s GPT‑4 Turbo or Anthropic’s Claude) via LangChain to process raw snippets.  
   - Identifies key market **trends**, **competitors**, **sentiment**, **market size**, **CAGR**, and **technical drivers**.  
   - Returns a structured JSON with those fields.

3. **Writer Agent**  
   - Takes the Analysis JSON and composes a comprehensive Markdown report.  
   - Sections include: Executive Summary, Key Market Trends, Market Size & Growth, Technical Drivers, Competitive Landscape, Consumer Sentiment, and Conclusion.

A lightweight **Orchestrator** in `workflow/graph.py` wires these agents together with retry logic if insufficient trends are found. A **Streamlit** front end (`ui/app.py`) provides a simple text box for topic input and displays the final report.

---

## Architecture & Workflow

```mermaid
flowchart TD
    A[Streamlit UI] -->|Enter topic| B[Orchestrator]
    B --> C[Research Agent]
    C --> D[Analysis Agent]
    D --> E[Writer Agent]
    E --> F[Final Report]


