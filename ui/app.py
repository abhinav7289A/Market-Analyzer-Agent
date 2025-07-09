import sys
import os
import streamlit as st

# Ensure parent dir is in sys.path so imports work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from workflow.graph import run_market_research_workflow

st.set_page_config(page_title="📊 Market Analyzer", layout="centered")

st.title("📊 Market Analyzer")
st.markdown("This app uses autonomous AI agents to research and generate detailed market reports.")

# User input
user_topic = st.text_input("Enter a topic (e.g., 'consumer drones')")

if st.button("Generate Report"):
    if not user_topic.strip():
        st.error("⚠️ Please enter a topic before generating the report.")
    else:
        with st.spinner("🔎 Running multi-agent workflow..."):
            # Construct input state
            initial_state = {"raw_data": user_topic.strip()}
            result = run_market_research_workflow(initial_state)

        if "report" in result:
            st.success("✅ Report Generated!")
            st.markdown(result["report"])
        elif "error" in result:
            st.error(f"❌ Workflow failed: {result['error']}")
        else:
            st.error("❌ Unknown failure occurred during the workflow.")
