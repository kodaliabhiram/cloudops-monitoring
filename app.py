import random
from datetime import datetime

def get_sample_metrics():
    """Generate sample cloud monitoring metrics."""
    return {
        "timestamp": datetime.now().isoformat(),
        "cpu_utilization": round(random.uniform(10, 95), 2),
        "memory_utilization": round(random.uniform(20, 90), 2),
        "disk_utilization": round(random.uniform(15, 85), 2),
    }


def detect_anomaly(metrics):
    """Detect unusually high resource utilization."""
    anomalies = []

    if metrics["cpu_utilization"] > 80:
        anomalies.append("High CPU utilization")

    if metrics["memory_utilization"] > 80:
        anomalies.append("High memory utilization")

    if metrics["disk_utilization"] > 80:
        anomalies.append("High disk utilization")

    return anomalies


if __name__ == "__main__":
    metrics = get_sample_metrics()
    anomalies = detect_anomaly(metrics)

    print("\nCloudOps Monitoring")
    print("-" * 30)
    print(f"Timestamp: {metrics['timestamp']}")
    print(f"CPU:      {metrics['cpu_utilization']}%")
    print(f"Memory:   {metrics['memory_utilization']}%")
    print(f"Disk:     {metrics['disk_utilization']}%")

    if anomalies:
        print("\n⚠️ Anomalies detected:")
        for anomaly in anomalies:
            print(f"- {anomaly}")
    else:
        print("\n✓ System operating normally")
