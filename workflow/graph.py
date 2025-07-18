import sys, os
import time

# Ensure project root is on Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from workflow.state import ResearchState
from agents.research_agent import run_researcher
from agents.analysis_agent import run_analyst
from agents.writer_agent import run_writer

# Orchestrator for the market research workflow

def run_market_research_workflow(state: ResearchState) -> ResearchState:
    """
    Orchestrator: state must contain 'topic' key prior to calling.
    """
    # Phase 1: Research
    print("▶️ [workflow entry] state:", state)
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
            time.sleep(1)
            state = run_researcher(state)
        else:
            break

    # Phase 3: Write
    state = run_writer(state)
    return state