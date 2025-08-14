# Heart Disease Prediction (FastAPI + Docker)

# 🌍 Live Render Deployment URL:  🔗 [Deployed on Render](https://fastapi-docker-heartdiseaseprediction.onrender.com/docs)






🫀 Heart Disease Prediction API

A FastAPI-powered REST API that serves predictions from a machine learning model trained to detect heart disease. This project focuses on containerization with Docker and deployment to the cloud using Render. Built as part of a hands-on assignment to demonstrate practical DevOps, ML, and API development skills.

🔍 Features

✅ /health — Health check endpoint

📄 /info — Returns model metadata

🔮 /predict — Accepts patient data and returns heart disease prediction (True/False)

🐳 Dockerized for local and cloud deployment

☁️ Live deployment on Render


🧠 Model

Trained on the Heart Disease UCI dataset

Model type: Random Forest Classifier

Saved using joblib and served as a REST API

🚀 Tech Stack

FastAPI

scikit-learn

Docker & Docker Compose

Render (for cloud deployment)

Pydantic (for input validation)

📦 Installation (Local)
bash
Copy
Edit
git clone https://github.com/yourusername/heart-disease-api.git
cd heart-disease-api
docker-compose up --build
Then visit: http://localhost:8000/docs

📦 Train model locally
```bash
python -m pip install -r requirements.txt
python train_model.py
# This will create model/heart_model.joblib

📁 Project Structure

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
```
![Screenshot](https://github.com/debbrath/FastAPI_Docker_HeartDiseasePrediction/blob/main/Image/2025-08-12%2013_54_19-Window.png)

![Screenshot](https://github.com/debbrath/FastAPI_Docker_HeartDiseasePrediction/blob/main/Image/2025-08-12%2013_57_32-Window.png)

![Screenshot](https://github.com/debbrath/FastAPI_Docker_HeartDiseasePrediction/blob/main/Image/2025-08-12%2016_55_08-Window.png)



✍️ Author

Debbrath Debnath

📫 [Connect on LinkedIn](https://www.linkedin.com/in/debbrathdebnath/)

🌐 [GitHub Profile](https://github.com/debbrath)

