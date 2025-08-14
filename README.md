# Heart Disease Prediction (FastAPI + Docker)

# 🌍 Live Render Deployment 
# 📦  Live API:  [Swagger Docs](https://heart-disease-prediction-joq2.onrender.com/docs)
# 📦  Live APPLICATION: [Heart Disease Prediction](https://fastapi-docker-heartdiseaseprediction.onrender.com)






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

FastAPI_Docker_HeartDiseasePrediction/
├─ app/
│  ├─ __init__.py
│  ├─ main.py               # Your FastAPI app code
│  ├─ schemas.py            # Pydantic schemas
│  ├─ utils.py              # Helper functions, model loading, predictions
│  └─ templates/
│     └─ index.html         # Your HTML template file
├─ model/
│  └─ heart_model.joblib    # Trained model file
├─ data/
│  └─ heart.csv             # Dataset file
├─ train_model.py           # Script to train model and save joblib file
├─ Dockerfile               # Docker build instructions
├─ docker-compose.yml       # (optional) docker-compose config
├─ requirements.txt         # Python dependencies
├─ README.md                # Project documentation
└─ .gitignore               # Git ignore rules

📸 Screenshots
```
![Screenshot](https://github.com/debbrath/FastAPI_Docker_HeartDiseasePrediction/blob/main/Image/2025-08-12%2013_54_19-Window.png)

![Screenshot](https://github.com/debbrath/FastAPI_Docker_HeartDiseasePrediction/blob/main/Image/2025-08-12%2013_57_32-Window.png)

![Screenshot](https://github.com/debbrath/FastAPI_Docker_HeartDiseasePrediction/blob/main/Image/2025-08-12%2016_55_08-Window.png)

![Screenshot](https://github.com/debbrath/FastAPI_Docker_HeartDiseasePrediction/blob/main/Image/2025-08-14%2011_59_10-Window.png)




✍️ Author

Debbrath Debnath

📫 [Connect on LinkedIn](https://www.linkedin.com/in/debbrathdebnath/)

🌐 [GitHub Profile](https://github.com/debbrath)

