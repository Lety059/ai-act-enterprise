import streamlit as st

st.title("Explorer KB")

kb = st.session_state.get("kb", {})

if not kb:
    st.error("KB non caricata.")
    st.stop()

articles = kb.get("articles", {})

if not articles:
    st.warning("Nessun articolo trovato.")
    st.stop()

article_id = st.selectbox(
    "Seleziona articolo",
    sorted(articles.keys())
)

data = articles.get(article_id)

st.subheader(data.get("title"))
st.write("Categoria:", data.get("category"))
st.write("Priorità:", data.get("priority"))

st.markdown("### Obblighi pratici")
for o in data.get("practical_obligations", []):
    st.write("-", o)

st.markdown("### Evidenze richieste")
for e in data.get("required_evidence", []):
    st.write("-", e)
