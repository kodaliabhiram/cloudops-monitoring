from fastapi import FastAPI
from app import get_sample_metrics, detect_anomaly

app = FastAPI(
    title="CloudOps Monitoring API",
    description="API for cloud resource monitoring and anomaly detection",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "CloudOps Monitoring API is running",
        "status": "healthy"
    }


@app.get("/metrics")
def metrics():
    data = get_sample_metrics()
    anomalies = detect_anomaly(data)

    return {
        "metrics": data,
        "anomalies": anomalies,
        "anomaly_detected": len(anomalies) > 0
    }
