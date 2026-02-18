import streamlit as st
from core.kb_loader import load_kb, kb_source_path

st.set_page_config(
    page_title="AI Act Enterprise",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded",
)

kb = load_kb()
n = len(kb.get("articles", {}))

st.title("AI Act Enterprise")

if n > 0:
    st.success(f"KB attiva, {n} articoli disponibili")
else:
    st.error("KB vuota, la compilazione non ha prodotto articoli")

with st.expander("Debug KB", expanded=False):
    st.write("Sorgente KB:", kb_source_path())
    st.write("Numero articoli:", n)
    st.write("Chiavi KB:", list(kb.keys()))

st.markdown("Apri le pagine dal menu laterale.")
