import streamlit as st
import requests
import pandas as pd

st.title("🧪 A/B Testing-as-a-Service")

uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Sample Data:", df.head())
    
    if st.button("Run A/B Test"):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://localhost:8000/analyze", files=files)
        result = response.json()
        st.write("Results:", result)
