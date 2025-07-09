from workflow.state import ResearchState

def run_writer(state: ResearchState) -> ResearchState:
    analysis = state.get("analysis", {})
    if not analysis:
        state["error"] = "No analysis to generate report."
        return state

    # Safely extract each field with fallback
    trends = analysis.get("trends", [])
    competitors = analysis.get("competitors", [])
    sentiment = analysis.get("sentiment", "N/A")
    market_size = analysis.get("market_size", "N/A")
    cagr = analysis.get("cagr", "N/A")
    technical_drivers = analysis.get("technical_drivers", [])

    # Compose the report
    report = f"""# Executive Summary
This report summarizes key insights on the consumer-grade drone market based on recent market data and trends.

## Key Market Trends
{chr(10).join([f"{i+1}. {trend}" for i, trend in enumerate(trends)])}

## Market Size & Growth
- **Market Size:** {market_size}
- **CAGR:** {cagr}

## Technical Drivers
{chr(10).join([f"- {tech}" for tech in technical_drivers]) if technical_drivers else "N/A"}

## Competitive Landscape
{", ".join(competitors) if competitors else "N/A"}

## Consumer Sentiment Analysis
{sentiment}

## Conclusion
The consumer drone market shows significant promise driven by ongoing technical innovations and strong consumer interest. However, factors like regulatory scrutiny and privacy concerns should be closely monitored.
"""
    # Update the state
    state["report"] = report
    return state
