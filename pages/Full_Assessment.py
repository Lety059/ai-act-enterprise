import streamlit as st
from core.kb_loader import load_kb

st.set_page_config(page_title="Full Assessment", page_icon="🧾", layout="centered")

kb = load_kb()
n = len(kb.get("articles", {}))

st.title("Full Assessment")
st.caption("Wizard completo, raccolta evidenze, stato di conformità, output audit-ready.")

if n == 0:
    st.error("KB vuota, impossibile procedere")
    st.stop()

st.info("Questa pagina è il contenitore del wizard completo. La struttura è pronta, ora si attaccano motori e template.")
st.write("Articoli disponibili:", n)

with st.expander("Seleziona articoli attivi per questo progetto", expanded=True):
    ids = sorted(kb["articles"].keys())
    selected = st.multiselect("Articoli", ids, default=ids[:5], key="full_selected_articles")
    st.write("Selezionati:", len(selected))

if st.button("Genera piano evidenze (stub)", use_container_width=True):
    st.success("Stub pronto. Nel prossimo step generiamo un manifest evidenze e i template Annex.")
