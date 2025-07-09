# run_analysis_test.py

from agents.analysis_agent import run_analyst
from workflow.state import ResearchState

# Example dummy raw_data (copy a couple of your real snippets here)
state: ResearchState = {
    "raw_data": [
        {
            "title": "Consumer Drone Market Revenue…",
            "source": "https://linkedin.com/…",
            "snippet": "Consumer Drone Market Revenue was valued at USD $19.6B in 2024…"
        },
        {
            "title": "DJI Drones in the U.S.…",
            "source": "https://dronelife.com/…",
            "snippet": "DJI drones … regulatory scrutiny…"
        }
    ]
}

updated = run_analyst(state)
if "analysis" in updated:
    print("Analysis JSON:")
    print(updated["analysis"])
else:
    print("Error:", updated.get("error"))

import json
with open("analysis_output.json", "w", encoding="utf-8") as f:
    json.dump(state["analysis"], f, indent=2, ensure_ascii=False)

print("\n✅ Analysis saved to analysis_output.json")