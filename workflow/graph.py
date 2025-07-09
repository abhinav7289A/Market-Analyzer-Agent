import sys, os
import time

# Ensure project root is on Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from workflow.state import ResearchState
from agents.research_agent import run_researcher
from agents.analysis_agent import run_analyst
from agents.writer_agent import run_writer

# Orchestrator for the market research workflow

def run_market_research_workflow(topic: str) -> ResearchState:
    # Initialize state with the user-defined topic
    state: ResearchState = {"topic": topic}

    # Phase 1: Research
    state = run_researcher(state)
    if "error" in state:
        return state

    # Phase 2: Analysis with retry logic
    for attempt in range(2):
        state = run_analyst(state)
        if "error" in state:
            return state
        trends = state.get("analysis", {}).get("trends", [])
        if len(trends) < 3:
            print(f"[Warning] Only {len(trends)} trends found; retrying research (attempt {attempt+2})...")
            time.sleep(1)
            state = run_researcher(state)
        else:
            break

    # Phase 3: Write report
    state = run_writer(state)
    return state

if __name__ == "__main__":
    topic = "consumer-grade drones in North America, last 6 months"
    final_state = run_market_research_workflow(topic)

    if "report" in final_state:
        print("\n=== Final Report ===\n")
        print(final_state["report"])
    else:
        print("Workflow failed with error:", final_state.get("error"))