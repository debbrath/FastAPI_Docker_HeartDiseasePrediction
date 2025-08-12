# app/utils.py
from pathlib import Path
import joblib
import numpy as np
import pandas as pd

MODEL_PATH = Path(__file__).resolve().parent.parent / "model" / "heart_model.joblib"

def load_model():
    obj = joblib.load(MODEL_PATH)
    pipeline = obj["pipeline"]
    meta = obj.get("meta", {})
    return pipeline, meta

def predict_from_dict(pipeline, input_dict):
    # convert to DataFrame so get_dummies aligns with training
    df = pd.DataFrame([input_dict])
    # Note: training used pd.get_dummies(drop_first=True) — to be safe, apply same transform here
    df = pd.get_dummies(df, drop_first=True)
    # Align columns: add missing columns with zeros
    # We expect pipeline to have been trained on fixed set; the pipeline's imputers will accept missing columns
    return pipeline.predict(df)[0], pipeline.predict_proba(df)[0][1]  # return class and probability of class 1