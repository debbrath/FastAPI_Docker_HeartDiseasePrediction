# app/main.py
from fastapi import FastAPI, HTTPException
from app.schemas import HeartInput
from app.utils import load_model, predict_from_dict
from typing import Dict

app = FastAPI(title="Heart Disease Prediction API")

pipeline, meta = load_model()
FEATURE_LIST = meta.get("feature_names", None)
MODEL_TYPE = meta.get("model_type", "unknown")
MODEL_ACC = meta.get("accuracy", None)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/info")
def info():
    return {
        "model_type": MODEL_TYPE,
        "model_accuracy": MODEL_ACC,
        "features": FEATURE_LIST
    }

@app.post("/predict")
def predict(payload: HeartInput):
    try:
        x = payload.dict()
        pred_class, prob = predict_from_dict(pipeline, x)
        # Map to boolean: assume 1 means disease present
        heart_disease = bool(int(pred_class))
        return {
            "heart_disease": heart_disease,
            "probability_disease": float(prob)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))