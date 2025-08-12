# app/schemas.py
from pydantic import BaseModel, Field
from typing import Optional

# Example fields (adjust names/types to match your CSV column names)
class HeartInput(BaseModel):
    age: float
    sex: int
    cp: int
    trestbps: float
    chol: float
    fbs: int
    restecg: int
    thalach: float
    exang: int
    oldpeak: float
    slope: int
    ca: Optional[float] = Field(None, description="number of major vessels (0-3)")
    thal: Optional[int] = None