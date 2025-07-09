# run_writer_test.py

from agents.writer_agent import run_writer
from workflow.state import ResearchState
import json

# Load the full analysis output from a file or hardcoded string
# If you saved analysis JSON earlier, load it like this:
with open("analysis_output.json", "r", encoding="utf-8") as f:
    analysis_data = json.load(f)

# OR paste the full real output here:
# analysis_data = {
#     "trends": [...],
#     "competitors": [...],
#     ...
# }

state: ResearchState = {
    "analysis": analysis_data
}

# DEBUG
print("Using analysis:")
print(json.dumps(state["analysis"], indent=2))

# Run writer
updated = run_writer(state)

# Print the final report
print("\n--- Report ---\n")
print(updated["report"])

