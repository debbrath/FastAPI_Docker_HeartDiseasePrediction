# app/main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.schemas import HeartInput
import joblib
import numpy as np
import os
from app import utils  # Import the whole module, avoids circular issues

pipeline = None
meta = None


app = FastAPI(title="Heart Disease Prediction API")
# Load model and metadata

@app.on_event("startup")
def load_pipeline():
    global pipeline, meta
    pipeline, meta = utils.load_model()

# Mount static directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/static")

# Serve index.html at /
@app.get("/", response_class=HTMLResponse)
async def serve_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/test", response_class=HTMLResponse)
def test_html():
    return "<h1>Hello World</h1>"

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/info")
def get_info():
    return {
        "model": "RandomForestClassifier",
        "features": [
            "age", "sex", "cp", "trestbps", "chol", "fbs",
            "restecg", "thalach", "exang", "oldpeak",
            "slope", "ca", "thal"
        ]
    }

@app.post("/predict")
def predict(data: HeartInput):
    input_dict = data.dict()
    print("🔍 INPUT:", input_dict)  # Debug log

    try:
        prediction, probability = utils.predict_from_dict(pipeline, input_dict)
        print(f"✅ Prediction: {prediction} | Probability: {probability:.4f}")  # Debug log
        return {
            "heart_disease": bool(prediction),
            "probability": round(probability, 4)
        }
    except Exception as e:
        print("❌ Error:", str(e))
        return {"error": str(e)}