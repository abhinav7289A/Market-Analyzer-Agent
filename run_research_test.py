# run_research_test.py

from agents.research_agent import run_researcher
from workflow.state import ResearchState
import os
from dotenv import load_dotenv

# load your .env keys so the SerpAPIWrapper can authenticate
load_dotenv()

# 1) Initialize state with your chosen topic
state: ResearchState = {
    "topic": "consumer-grade drones in North America, last 6 months"
}

# 2) Run the researcher agent
updated_state = run_researcher(state)

# 3) Inspect the raw_data
raw = updated_state.get("raw_data", [])
print(f"Found {len(raw)} snippets:")
for i, entry in enumerate(raw, start=1):
    print(f"{i}. {entry['title']} — {entry['source']}")
    print(f"   “{entry['snippet']}”\n")