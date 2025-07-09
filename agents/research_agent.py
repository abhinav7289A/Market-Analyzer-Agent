# agents/research_agent.py

import os
from dotenv import load_dotenv
from serpapi import GoogleSearch
from workflow.state import ResearchState

load_dotenv()
API_KEY = os.getenv("SERPER_API_KEY") or os.getenv("SERPAPI_KEY")

def run_researcher(state: ResearchState) -> ResearchState:
    topic = state.get("topic", "")
    if not topic:
        state["error"] = "No topic provided to researcher agent."
        return state

    query = f"latest articles and data on {topic}"
    params = {"q": query, "api_key": API_KEY, "num": 5}
    search = GoogleSearch(params)
    results = search.get_dict().get("organic_results", [])

    snippets = []
    for item in results:
        snippets.append({
            "source": item.get("link", ""),
            "title": item.get("title", ""),
            "snippet": item.get("snippet", ""),
        })
        
    seen = set()
    cleaned = []
    for item in snippets:
        url = item["source"]
        if url in seen or not url:
            continue
        item["snippet"] = item["snippet"].strip()
        cleaned.append(item)
        seen.add(url)

    state["raw_data"] = cleaned
    return state
