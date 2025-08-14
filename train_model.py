from imblearn.pipeline import Pipeline  # ✅ Use imblearn's pipeline
from imblearn.over_sampling import SMOTE  # ✅ Import SMOTE
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from pathlib import Path
import pandas as pd
import joblib

DATA_PATH = Path("data/heart.csv")
MODEL_DIR = Path("model")
MODEL_DIR.mkdir(exist_ok=True)

def load_data(path=DATA_PATH):
    df = pd.read_csv(path)
    if 'target' in df.columns:
        target_col = 'target'
    elif 'HeartDisease' in df.columns:
        target_col = 'HeartDisease'
    elif 'heart_disease' in df.columns:
        target_col = 'heart_disease'
    else:
        raise ValueError("Couldn't find target column. Please check CSV columns: " + ", ".join(df.columns))
    X = df.drop(columns=[target_col])
    y = df[target_col]
    return X, y

def train():
    X, y = load_data()
    X = pd.get_dummies(X, drop_first=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("smote", SMOTE(random_state=42)),  # ✅ Apply SMOTE after scaling
        ("clf", RandomForestClassifier(n_estimators=100, random_state=42))
    ])

    pipeline.fit(X_train, y_train)
    acc = pipeline.score(X_test, y_test)
    print(f"Test accuracy: {acc:.4f}")

    model_path = MODEL_DIR / "heart_model.joblib"
    meta = {
        "feature_names": list(X.columns),
        "model_type": "RandomForestClassifier with SMOTE",
        "accuracy": float(acc)
    }
    joblib.dump({"pipeline": pipeline, "meta": meta}, model_path)
    print(f"Saved model to {model_path}")

if __name__ == "__main__":
    train()