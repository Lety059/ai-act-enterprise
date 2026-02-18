import json
import os
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "kb" / "act" / "articles"
OUT_DIR = ROOT / "kb" / "runtime"
OUT_FILE = OUT_DIR / "compiled_kb.json"

def norm_str(x):
    if x is None:
        return ""
    return str(x).strip()

def load_articles():
    articles = {}
    if not SRC_DIR.exists():
        return articles

    for p in sorted(SRC_DIR.glob("*.yaml")):
        try:
            obj = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        except Exception:
            continue

        art_id = norm_str(obj.get("id"))
        if not art_id:
            stem = p.stem.upper()
            art_id = stem if stem.startswith("A") else f"A{stem}"

        art_id = art_id.upper()
        title = norm_str(obj.get("title")) or norm_str(obj.get("titolo")) or "Senza titolo"

        articles[art_id] = {
            "id": art_id,
            "title": title,
            "category": norm_str(obj.get("category") or obj.get("categoria") or "GENERAL"),
            "priority": norm_str(obj.get("priority") or obj.get("priorita") or "MEDIUM"),
            "owner": norm_str(obj.get("owner") or obj.get("proprietario") or ""),
            "evidence_needed": obj.get("evidence_needed") or obj.get("evidenza_richiesta") or "",
            "practical_obligations": obj.get("practical_obligations") or obj.get("obblighi_pratici") or [],
            "required_evidence": obj.get("required_evidence") or obj.get("prove_richieste") or [],
            "completeness_status": norm_str(obj.get("completeness_status") or obj.get("stato_completezza") or ""),
        }

    return articles

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    articles = load_articles()

    payload = {
        "articles": articles,
        "statistics": {
            "compiled_from": str(SRC_DIR),
            "count": len(articles),
        },
    }

    OUT_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Compiled: {len(articles)} articles")

if __name__ == "__main__":
    main()
