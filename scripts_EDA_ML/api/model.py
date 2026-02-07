import json
import os
from pathlib import Path

import joblib
import pandas as pd

DEFAULT_MODEL_PATH = "artifacts/model.joblib"
DEFAULT_METADATA_PATH = "artifacts/metadata.json"

_model = None
_metadata = None


def load_metadata(path: str) -> dict:
    p = Path(path)
    if not p.exists():
        return {}
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


def get_model():
    global _model, _metadata

    if _model is None:
        model_path = os.getenv("MODEL_PATH", DEFAULT_MODEL_PATH)
        metadata_path = os.getenv("METADATA_PATH", DEFAULT_METADATA_PATH)

        _metadata = load_metadata(metadata_path)
        _model = joblib.load(model_path)

    return _model, (_metadata or {})


def predict_one(payload: dict) -> dict:
    model, metadata = get_model()

    features_all = metadata.get(
        "features_all",
        ["Idade", "Tempo_de_Casa", "Defasagem", "IDA", "IEG", "IPS", "IPP", "IAA", "Gênero", "Instituicao_ensino"],
    )

    row = {k: payload.get(k) for k in features_all}
    X = pd.DataFrame([row])

    pred = int(model.predict(X)[0])
    proba = None
    if hasattr(model, "predict_proba"):
        proba = float(model.predict_proba(X)[0, 1])

    return {"atingiu_pv": pred, "proba": proba}
