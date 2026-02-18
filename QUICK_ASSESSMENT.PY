import streamlit as st

st.title("Quick Assessment")

kb = st.session_state.get("kb", {})

if not kb:
    st.error("KB non caricata.")
    st.stop()

st.write("Numero articoli KB:", len(kb.get("articles", {})))

domain = st.selectbox(
    "Dominio applicativo",
    ["Seleziona", "HR", "Finance", "Healthcare", "Public Sector"]
)

impact = st.selectbox(
    "Impatto decisionale",
    ["Seleziona", "Basso", "Medio", "Alto"]
)

if st.button("Calcola rischio"):
    if domain == "Seleziona" or impact == "Seleziona":
        st.warning("Compila tutti i campi.")
    else:
        if impact == "Alto":
            risk = "HIGH"
        elif impact == "Medio":
            risk = "MEDIUM"
        else:
            risk = "LOW"

        st.success(f"Rischio preliminare: {risk}")
