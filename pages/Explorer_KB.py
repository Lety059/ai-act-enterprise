import streamlit as st
from core.kb_loader import load_kb

st.set_page_config(page_title="Explorer KB", page_icon="📚", layout="centered")

kb = load_kb()
articles = kb.get("articles", {})
count = len(articles)

st.title("Explorer KB")

if count == 0:
    st.error("KB vuota. Verifica kb/runtime/compiled_kb.json e la compilazione su Render.")
    st.stop()

st.success(f"{count} articoli caricati")

ids_all = sorted(articles.keys())

search = st.text_input("Cerca (id o titolo)", value="", placeholder="es. A011 oppure documentazione")

if search.strip():
    q = search.strip().lower()
    ids = [i for i in ids_all if q in i.lower() or q in str(articles[i].get("title","")).lower()]
else:
    ids = ids_all

if not ids:
    st.warning("Nessun articolo trovato con questo filtro")
    st.stop()

default_id = st.query_params.get("a")
if isinstance(default_id, list) and default_id:
    default_id = default_id[0]

if not default_id or default_id not in ids:
    default_id = ids[0]

index = ids.index(default_id)

def _fmt(x):
    t = articles.get(x, {}).get("title", "")
    return f"{x}   {t}"

selected = st.selectbox(
    "Seleziona articolo",
    options=ids,
    index=index,
    format_func=_fmt,
    key="kb_selected_id",
)

st.query_params["a"] = selected

art = articles[selected]

st.markdown("---")
st.header(f"{art.get('id','')}  {art.get('title','')}")

c1, c2 = st.columns(2)
with c1:
    st.caption("Categoria")
    st.write(str(art.get("category", "GENERAL")).upper())
with c2:
    st.caption("Priorità")
    st.write(str(art.get("priority", "MEDIUM")).upper())

owner = art.get("owner") or ""
if owner:
    st.caption("Titolare")
    st.write(owner)

st.subheader("Obblighi pratici")
obs = art.get("practical_obligations") or []
if obs:
    for x in obs:
        st.write(f"• {x}")
else:
    st.info("Nessun obbligo pratico presente")

st.subheader("Evidenza richiesta")
ev = art.get("required_evidence") or []
if ev:
    for x in ev:
        st.write(f"• {x}")
else:
    st.info("Nessuna evidenza richiesta presente")
