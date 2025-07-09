import sys, os
import streamlit as st

# Make sure project root is on the path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from workflow.graph import run_market_research_workflow

st.set_page_config(page_title="📊 Market Analyzer", layout="centered")
st.title("📊 Market Analyzer")
st.markdown("This app uses autonomous AI agents to research and generate detailed market reports.")

topic = st.text_input("Enter a topic (e.g., 'consumer drones')")

if st.button("Generate Report"):
    if not topic.strip():
        st.error("⚠️ Please enter a topic.")
    else:
        with st.spinner("🔎 Running workflow..."):
            # Pass full state dict
            state = {"topic": topic.strip()}
            result = run_market_research_workflow(state)

        if "report" in result:
            st.success("✅ Report Generated!")
            st.markdown(result["report"])
        else:
            st.error(f"❌ Workflow failed: {result.get('error', 'Unknown error')}")
