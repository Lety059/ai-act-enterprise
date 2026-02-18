import json
import os
from pathlib import Path
import streamlit as st

def _candidate_paths():
    here = Path(__file__).resolve()
    root = here.parent.parent
    return [
        root / "kb" / "runtime" / "compiled_kb.json",
        Path.cwd() / "kb" / "runtime" / "compiled_kb.json",
    ]

def _normalize_kb(data: dict) -> dict:
    if not isinstance(data, dict):
        return {"articles": {}, "statistics": {}}

    articles = data.get("articles")
    if articles is None:
        articles = data.get("articoli")

    statistics = data.get("statistics")
    if statistics is None:
        statistics = data.get("statistiche")

    if not isinstance(articles, dict):
        articles = {}

    if not isinstance(statistics, dict):
        statistics = {}

    return {"articles": articles, "statistics": statistics}

@st.cache_data(show_spinner=False)
def load_kb() -> dict:
    for p in _candidate_paths():
        try:
            if p.exists():
                raw = p.read_text(encoding="utf-8")
                data = json.loads(raw)
                return _normalize_kb(data)
        except Exception:
            continue

    return {"articles": {}, "statistics": {}}

def kb_source_path() -> str:
    for p in _candidate_paths():
        if p.exists():
            return str(p)
    return "kb/runtime/compiled_kb.json non trovata"
