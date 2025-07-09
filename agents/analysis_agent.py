import os
import json
from dotenv import load_dotenv
from anthropic import Anthropic
from workflow.state import ResearchState

# Load environment variables
load_dotenv()
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
client = Anthropic(api_key=ANTHROPIC_API_KEY)

# Improved system message with explicit JSON structure
SYSTEM_PROMPT = (
    "You are a senior market analyst.\n"
    "Given the following raw research data (a list of items with title, URL, and snippet),\n"
    "perform an in-depth market analysis.\n\n"
    "Return ONLY a valid JSON object with these keys:\n"
    "- trends: array of 3–5 major market trends\n"
    "- competitors: array of company names\n"
    "- sentiment: 1–2 sentence consumer sentiment summary\n"
    "- market_size: Estimated total market size with currency and year (e.g., 'USD 19.6B in 2024')\n"
    "- cagr: CAGR in percentage with years (e.g., '8.3% CAGR from 2024 to 2030')\n"
    "- technical_drivers: array of 2–4 technical innovations (e.g., 'AI-based stabilization')\n\n"
    "Ensure strict JSON format. Do NOT repeat keys."
)

def run_analyst(state: ResearchState) -> ResearchState:
    # Retrieve raw data
    raw_data = state.get("raw_data", [])
    if not raw_data:
        state["error"] = "No raw_data for analysis."
        return state

    # Format raw_data as JSON string
    raw_json = json.dumps(raw_data, ensure_ascii=False, indent=2)

    # Use the Claude 3 Messages API
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        temperature=0.2,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": raw_json}
        ]
    )

    # Extract and parse response
    content = response.content[0].text.strip()
    try:
        analysis = json.loads(content)
    except json.JSONDecodeError:
        state["error"] = f"Failed to parse JSON: {content}"
        return state

    # Update state with structured analysis
    state["analysis"] = analysis
    return state
