import os
import json
import streamlit as st

st.set_page_config(
    page_title="AI Act Enterprise",
    layout="wide"
)

def load_kb():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    kb_path = os.path.join(base_dir, "kb", "runtime", "compiled_kb.json")

    if not os.path.exists(kb_path):
        st.error(f"KB non trovata in: {kb_path}")
        return {}

    with open(kb_path, "r", encoding="utf-8") as f:
        return json.load(f)

if "kb" not in st.session_state:
    st.session_state.kb = load_kb()

st.title("AI ACT ENTERPRISE")
st.markdown("Seleziona una sezione dal menu laterale.")
