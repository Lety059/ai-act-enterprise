import streamlit as st

st.title("Full Assessment")

kb = st.session_state.get("kb", {})

if not kb:
    st.error("KB non caricata.")
    st.stop()

st.write("Totale articoli:", len(kb.get("articles", {})))

selected = st.multiselect(
    "Seleziona articoli applicabili",
    list(kb.get("articles", {}).keys())
)

if st.button("Analizza"):
    if not selected:
        st.warning("Seleziona almeno un articolo.")
    else:
        for art in selected:
            article_data = kb["articles"].get(art)
            st.subheader(art)
            st.write("Titolo:", article_data.get("title"))
            st.write("Priorità:", article_data.get("priority"))
