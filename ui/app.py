import sys, os
import streamlit as st

# Ensure project root is on path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from workflow.graph import run_market_research_workflow

st.set_page_config(page_title="📊 Market Analyzer", layout="centered")
st.title("📊 Market Analyzer")
st.markdown("This app uses autonomous AI agents to research and generate detailed market reports.")

user_topic = st.text_input("Enter a topic (e.g., 'consumer drones')")

if st.button("Generate Report"):
    if not user_topic.strip():
        st.error("⚠️ Please enter a topic before generating the report.")
    else:
        with st.spinner("🔎 Running multi-agent workflow..."):
            # Pass the topic in the correct key
            initial_state = {"topic": user_topic.strip()}
            result = run_market_research_workflow(initial_state)

        if "report" in result:
            st.success("✅ Report Generated!")
            st.markdown(result["report"])
        elif "error" in result:
            st.error(f"❌ Workflow failed: {result['error']}")
        else:
            st.error("❌ Unknown failure occurred during the workflow.")
