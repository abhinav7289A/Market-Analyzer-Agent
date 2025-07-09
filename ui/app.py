import sys, os
# Ensure project root is on path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from workflow.graph import run_market_research_workflow
from workflow.state import ResearchState

st.set_page_config(page_title="Multi‑Agent Market Research", layout="centered")

st.title("Multi‑Agent Market Research System")

# User input for research topic
topic = st.text_input(
    "Enter your research topic:",
    value="consumer-grade drones in North America, last 6 months"
)

if st.button("Generate Report"):
    with st.spinner("Running multi-agent workflow..."):
        final_state: ResearchState = run_market_research_workflow(topic)
        if "report" in final_state:
            st.markdown(final_state["report"])
        else:
            st.error(f"Workflow failed: {final_state.get('error')}")