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
    import pandas as pd

    df = pd.DataFrame([input_dict])
    df = pd.get_dummies(df, drop_first=True)

    # Align prediction features with training features
    for col in pipeline.feature_names_in_:
        if col not in df.columns:
            df[col] = 0
    df = df[pipeline.feature_names_in_]

    prediction = pipeline.predict(df)[0]
    probability = pipeline.predict_proba(df)[0][1]
    return prediction, probability