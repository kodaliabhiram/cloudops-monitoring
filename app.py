import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.ensemble import IsolationForest
from datetime import datetime

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="CloudOps Monitoring",
    page_icon="☁️",
    layout="wide"
)

st.title("☁️ CloudOps Monitoring Dashboard")
st.markdown(
    "Real-time style cloud infrastructure monitoring "
    "with machine-learning based anomaly detection."
)

# -----------------------------
# Generate monitoring data
# -----------------------------
@st.cache_data
def generate_metrics(n=100):
    np.random.seed(42)

    timestamps = pd.date_range(
        end=datetime.now(),
        periods=n,
        freq="min"
    )

    cpu = np.random.normal(55, 12, n)
    memory = np.random.normal(60, 10, n)
    disk = np.random.normal(50, 8, n)

    # Add a few abnormal points
    cpu[20] = 95
    cpu[70] = 92
    memory[45] = 94
    disk[80] = 91

    df = pd.DataFrame({
        "timestamp": timestamps,
        "cpu_utilization": np.clip(cpu, 0, 100),
        "memory_utilization": np.clip(memory, 0, 100),
        "disk_utilization": np.clip(disk, 0, 100)
    })

    return df


df = generate_metrics()

# -----------------------------
# ML anomaly detection
# -----------------------------
features = [
    "cpu_utilization",
    "memory_utilization",
    "disk_utilization"
]

model = IsolationForest(
    contamination=0.05,
    random_state=42
)

df["anomaly"] = model.fit_predict(df[features])

df["status"] = np.where(
    df["anomaly"] == -1,
    "Anomaly",
    "Normal"
)

# -----------------------------
# Current metrics
# -----------------------------
latest = df.iloc[-1]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "CPU Usage",
        f"{latest['cpu_utilization']:.1f}%"
    )

with col2:
    st.metric(
        "Memory Usage",
        f"{latest['memory_utilization']:.1f}%"
    )

with col3:
    st.metric(
        "Disk Usage",
        f"{latest['disk_utilization']:.1f}%"
    )

with col4:
    anomaly_count = (df["anomaly"] == -1).sum()
    st.metric(
        "Anomalies Detected",
        anomaly_count
    )

# -----------------------------
# CPU chart
# -----------------------------
st.subheader("📈 CPU Utilization")

fig_cpu = px.line(
    df,
    x="timestamp",
    y="cpu_utilization",
    title="CPU Usage Over Time"
)

fig_cpu.add_hline(
    y=80,
    line_dash="dash",
    annotation_text="Warning Threshold"
)

st.plotly_chart(
    fig_cpu,
    use_container_width=True
)

# -----------------------------
# Memory and disk charts
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("🧠 Memory Utilization")

    fig_memory = px.line(
        df,
        x="timestamp",
        y="memory_utilization",
        title="Memory Usage"
    )

    fig_memory.add_hline(
        y=80,
        line_dash="dash"
    )

    st.plotly_chart(
        fig_memory,
        use_container_width=True
    )

with col2:
    st.subheader("💾 Disk Utilization")

    fig_disk = px.line(
        df,
        x="timestamp",
        y="disk_utilization",
        title="Disk Usage"
    )

    fig_disk.add_hline(
        y=80,
        line_dash="dash"
    )

    st.plotly_chart(
        fig_disk,
        use_container_width=True
    )

# -----------------------------
# Anomaly table
# -----------------------------
st.subheader("🚨 Detected Anomalies")

anomalies = df[df["anomaly"] == -1].copy()

if len(anomalies) > 0:
    st.dataframe(
        anomalies[
            [
                "timestamp",
                "cpu_utilization",
                "memory_utilization",
                "disk_utilization",
                "status"
            ]
        ],
        use_container_width=True
    )
else:
    st.success("No anomalies detected.")

# -----------------------------
# Monitoring summary
# -----------------------------
st.subheader("📊 Monitoring Summary")

summary = pd.DataFrame({
    "Metric": [
        "Average CPU",
        "Average Memory",
        "Average Disk",
        "Total Data Points",
        "Detected Anomalies"
    ],
    "Value": [
        f"{df['cpu_utilization'].mean():.2f}%",
        f"{df['memory_utilization'].mean():.2f}%",
        f"{df['disk_utilization'].mean():.2f}%",
        len(df),
        anomaly_count
    ]
})

st.table(summary)

st.markdown("---")

st.caption(
    "CloudOps Monitoring | Python • Streamlit • Plotly • Scikit-learn"
)
