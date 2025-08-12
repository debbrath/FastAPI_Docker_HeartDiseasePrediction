# Heart Disease Prediction — FastAPI + Docker

## Contents
- `train_model.py` — trains a RandomForest and saves `model/heart_model.joblib`
- `app/` — FastAPI app
- `Dockerfile`, `docker-compose.yml`, `requirements.txt`

## 1) Prepare data
Download the Kaggle Heart Disease dataset and put `heart.csv` in `data/heart.csv`.

## 2) Train model locally
```bash
python -m pip install -r requirements.txt
python train_model.py
# This will create model/heart_model.joblib


heart-fastapi/
├─ app/
│  ├─ main.py
│  ├─ schemas.py
│  ├─ utils.py
├─ model/
│  └─ (after training) heart_model.joblib
├─ data/
│  └─ heart.csv    # put Kaggle CSV here
├─ train_model.py
├─ Dockerfile
├─ docker-compose.yml
├─ requirements.txt
├─ README.md
└─ .gitignore

📸 Screenshots

![Screenshot](https://github.com/debbrath/FastAPI_Docker_HeartDiseasePrediction/blob/main/Image/2025-08-12%2013_54_19-Window.png)

![alt text](<Image/2025-08-12 13_54_19-Window.png>)
