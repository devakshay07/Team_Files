import streamlit as st
import requests
import json

API_URL = "http://localhost:8000/analyze"

st.set_page_config(page_title="SIF Precursor Analysis", layout="wide")

st.title("SIF Precursor Detection Engine")
st.markdown("Analyze safety reports for potential Serious Injury & Fatality precursors.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Input Report")
    report_type = st.selectbox("Report Type", ["Unsafe Act", "Unsafe Condition", "Near Miss"])
    location = st.text_input("Location (Optional)", "Unit A")
    equipment = st.text_input("Equipment (Optional)", "Pump")
    report_text = st.text_area("Report Description", height=200, placeholder="Describe the incident or condition...")
    
    if st.button("Analyze Report", type="primary"):
        if not report_text.strip():
            st.error("Please enter a report description.")
        else:
            with st.spinner("Analyzing with AI Engine..."):
                payload = {
                    "text": report_text,
                    "report_type": report_type,
                    "location": location,
                    "equipment": equipment
                }
                try:
                    response = requests.post(API_URL, json=payload)
                    response.raise_for_status()
                    result = response.json()
                    
                    with col2:
                        st.subheader("AI Analysis Result")
                        
                        risk = result.get("risk_level", "UNKNOWN")
                        conf = result.get("confidence", 0.0)
                        human_review = result.get("human_review_recommended", False)
                        
                        color = "green"
                        if risk == "MEDIUM": color = "orange"
                        elif risk == "HIGH": color = "red"
                        elif risk == "CRITICAL": color = "darkred"
                        
                        st.markdown(f"### SIF Risk: <span style='color:{color}'>{risk}</span> (Confidence: {conf:.0%})", unsafe_allow_html=True)
                        
                        if human_review:
                            st.warning("⚠️ **HUMAN REVIEW RECOMMENDED:** The model confidence is borderline, or the NLP logic conflicts with the ML output.")
                            
                        st.markdown("#### Detected Precursors (Domain NLP)")
                        precursors = result.get("detected_precursors", [])
                        if precursors:
                            for p in precursors:
                                st.markdown(f"- {p}")
                        else:
                            st.markdown("*None explicitly detected by rule engine.*")
                            
                        st.markdown("#### Supporting Evidence (ML Weights)")
                        keywords = result.get("supporting_evidence", {}).get("keywords", [])
                        if keywords:
                            st.markdown(f"**Keywords:** {', '.join(keywords)}")
                        else:
                            st.markdown("*No strong ML features triggered.*")
                            
                        st.markdown("---")
                        st.caption("Note: This AI tool is for decision support only. Do not replace human safety judgment.")
                        st.caption(f"Model Version: {result.get('analytics_metadata', {}).get('model_version', 'Unknown')}")
                except Exception as e:
                    st.error(f"API Error: {e}")
