from typing import TypedDict, List

class ResearchState(TypedDict, total=False):
    topic: str               # e.g., "consumer-grade drones in North America, last 6 months"
    raw_data: List[dict]     # [{"source": "url", "snippet": "...", "timestamp": "..."}]
    analysis: dict           # {"trends": [...], "competitors": [...], "sentiment": "..."}
    report: str              # final markdown report
    error: str               # error message if something goes wrong