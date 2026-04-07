import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.preprocessing import load_data, clean_data
from src.analysis import state_wise_cases, year_trend, top_states
from src.model import train_model

st.set_page_config(page_title="Crime Analytics", layout="wide")

st.title("🚔 Crime Analysis & Prediction Dashboard")

# Load Data
df = load_data()
df = clean_data(df)

# Sidebar
st.sidebar.header("Filter")
year = st.sidebar.selectbox("Select Year", sorted(df['Year'].unique()))

filtered_df = df[df['Year'] == year]

# Dataset Preview
st.subheader("📊 Dataset Preview")
st.dataframe(filtered_df.head())

# State-wise Cases
st.subheader("📍 Cases by State")
state_data = state_wise_cases(filtered_df)
st.bar_chart(state_data)

# Year Trend
st.subheader("📈 Crime Trend Over Years")
trend = year_trend(df)
st.line_chart(trend)

# Top States
st.subheader("🔥 Top 5 States")
top = top_states(df)
st.bar_chart(top)

# Map (basic)
st.subheader("🗺️ Location Map (if lat-long available)")
if 'Latitude' in df.columns and 'Longitude' in df.columns:
    st.map(df[['Latitude', 'Longitude']])
else:
    st.info("Latitude/Longitude not available")

# ML Model
st.subheader("🤖 ML Prediction Model")
model, acc = train_model(df)

st.success(f"Model Accuracy: {round(acc*100, 2)}%")