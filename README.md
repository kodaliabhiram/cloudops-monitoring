# ☁️ CloudOps Monitoring & ML Anomaly Detection

A Python-based cloud infrastructure monitoring dashboard that tracks CPU, memory, and disk utilization and detects abnormal resource usage using machine-learning techniques.

## 🚀 Live Demo

**Live Dashboard:**  
https://cloudops-monitoring.onrender.com

---

## 📌 Project Overview

CloudOps Monitoring is a monitoring and anomaly-detection application designed to provide a real-time style view of cloud infrastructure health.

The application collects infrastructure metrics, analyzes resource utilization, detects abnormal behavior, and presents the results through an interactive Streamlit dashboard.

---

## ✨ Features

- 📊 CPU utilization monitoring
- 💾 Memory utilization monitoring
- 💿 Disk utilization monitoring
- 🚨 Resource anomaly detection
- 📈 Interactive monitoring charts
- 🌐 Streamlit web dashboard
- ⚡ FastAPI backend
- 🤖 Machine-learning-based anomaly detection
- 🐳 Docker containerization
- ☁️ Cloud deployment using Render

---

## 🏗️ Architecture

```text
Infrastructure Metrics
        ↓
Python Backend
        ↓
Metric Processing
        ↓
Anomaly Detection
        ↓
FastAPI API
        ↓
Streamlit Dashboard
        ↓
Monitoring & Visualization
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Application development |
| Streamlit | Monitoring dashboard |
| FastAPI | Backend API |
| Scikit-learn | Machine learning / anomaly detection |
| Pandas | Data processing |
| NumPy | Numerical processing |
| Plotly | Data visualization |
| Docker | Containerization |
| Render | Cloud deployment |

---

## 📂 Project Structure

```text
cloudops-monitoring/
│
├── app.py
├── api.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

### File Description

- `app.py` — Streamlit monitoring dashboard
- `api.py` — FastAPI backend
- `requirements.txt` — Python dependencies
- `Dockerfile` — Docker configuration for deployment
- `.dockerignore` — Files excluded from the Docker build context
- `README.md` — Project documentation

---

## 🤖 Anomaly Detection

The application analyzes infrastructure resource utilization and identifies unusual behavior using machine-learning techniques.

The dashboard displays detected anomalies alongside resource utilization metrics to help identify abnormal system behavior.

---

## 🐳 Docker

The application includes a Dockerfile for containerized deployment.

The container runs the Streamlit dashboard on port `8501`.

### Build the Docker image

```bash
docker build -t cloudops-monitoring .
```

### Run the Docker container

```bash
docker run -p 8501:8501 cloudops-monitoring
```

The dashboard can then be accessed at:

```text
http://localhost:8501
```

---

## ☁️ Deployment

The application is deployed using Docker on Render.

### Live Application

https://cloudops-monitoring.onrender.com

### Deployment Stack

- Python
- Streamlit
- FastAPI
- Docker
- Render
- Machine Learning

---

## ▶️ Run Locally Without Docker

### 1. Clone the repository

```bash
git clone https://github.com/kodaliabhiram/cloudops-monitoring.git
cd cloudops-monitoring
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the Streamlit dashboard

```bash
streamlit run app.py
```

The dashboard will be available at:

```text
http://localhost:8501
```

---

## 🔌 FastAPI Backend

The project also includes a FastAPI backend.

To start the API locally:

```bash
uvicorn api:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 📊 Dashboard

The dashboard provides monitoring information such as:

- CPU usage
- Memory usage
- Disk usage
- Resource utilization trends
- Warning thresholds
- Detected anomalies

The live dashboard is available here:

**https://cloudops-monitoring.onrender.com**

---

## 🔮 Future Improvements

Possible improvements include:

- AWS CloudWatch integration
- Real-time cloud infrastructure metrics
- Email or Slack alerts
- Persistent metric storage
- Advanced anomaly-detection models
- Kubernetes monitoring
- Automated CI/CD deployment
- Authentication and user management

---

## 👨‍💻 Author

**Abhiram Kodali**

GitHub:  
https://github.com/kodaliabhiram

---

## 📄 License

This project is intended for educational and demonstration purposes.
