from fastapi import FastAPI
from .schemas import PredictRequest, PredictResponse
from .model import get_model, predict_one

app = FastAPI(title="Datathon Med 2025 API", version="1.0.0")


@app.on_event("startup")
def _startup():
    get_model()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    result = predict_one(req.model_dump())
    return PredictResponse(**result, model_version="v1")
