import streamlit as st
from core.kb_loader import load_kb

st.set_page_config(page_title="Quick Assessment", page_icon="⚡", layout="centered")

kb = load_kb()
n = len(kb.get("articles", {}))

st.title("Quick Assessment")
st.caption("Valutazione rapida, deterministica, utile per triage interno.")

if n == 0:
    st.error("KB vuota, impossibile procedere")
    st.stop()

use_case = st.text_area("Descrivi il sistema o caso d’uso", placeholder="Cosa fa, per chi, con quali dati, in quale contesto")
domain = st.selectbox("Dominio", ["Generico", "HR", "Sanità", "Finanza", "Educazione", "Sicurezza", "Altro"])
deployed = st.selectbox("Il sistema è già in produzione", ["No", "Sì"])

if st.button("Esegui Quick Score", use_container_width=True):
    score = 0
    if deployed == "Sì":
        score += 2
    if domain in ["Sanità", "Finanza", "HR", "Educazione", "Sicurezza"]:
        score += 2
    if len(use_case.strip()) > 120:
        score += 1

    if score >= 4:
        band = "ALTO"
    elif score >= 2:
        band = "MEDIO"
    else:
        band = "BASSO"

    st.success(f"Esito rapido, banda: {band}")
    st.write("Prossimo passo consigliato: Full Assessment e generazione evidenze.")
