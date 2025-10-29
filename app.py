import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os
import gdown  # <— new import for downloading from Google Drive

# --------------------------
# Download model if not found
# --------------------------
MODEL_PATH = "my_california_housing_model.pkl"


FILE_ID = "1NKaaPmNzGGIZUeiASFcJWYIAgYynNC4l"
URL = f"https://drive.google.com/file/d/1NKaaPmNzGGIZUeiASFcJWYIAgYynNC4l/view?usp=sharing={FILE_ID}"

if not os.path.exists(MODEL_PATH):
    with st.spinner("Downloading model file..."):
        gdown.download(URL, MODEL_PATH, quiet=False)

# Load model
model = joblib.load(MODEL_PATH)

# --------------------------
# Streamlit App
# --------------------------
st.title("🏠 California House Price Prediction")

st.sidebar.header("Enter House Details:")

longitude = st.sidebar.slider("Longitude", -124.0, -114.0, -119.0)
latitude = st.sidebar.slider("Latitude", 32.0, 42.0, 36.0)
housing_median_age = st.sidebar.slider("Median Age of House", 1, 60, 25)
total_rooms = st.sidebar.number_input("Total Rooms", value=1500.0, step=100.0)
total_bedrooms = st.sidebar.number_input("Total Bedrooms", value=300.0, step=50.0)
median_income = st.sidebar.number_input("Median Income (×10,000 USD)", value=3.0, step=0.5)
ocean_proximity = st.sidebar.selectbox(
    "Ocean Proximity",
    ["<1H OCEAN", "INLAND", "NEAR BAY", "NEAR OCEAN"]
)

if st.button("Predict House Value"):
    input_data = pd.DataFrame([{
        'longitude': longitude,
        'latitude': latitude,
        'housing_median_age': housing_median_age,
        'total_rooms': total_rooms,
        'total_bedrooms': total_bedrooms,
        'population': total_rooms / 2,
        'households': total_bedrooms / 1.5,
        'median_income': median_income,
        'ocean_proximity': ocean_proximity
    }])

    input_data["income_cat"] = pd.cut(
        input_data["median_income"],
        bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
        labels=[1, 2, 3, 4, 5]
    )

    try:
        prediction = model.predict(input_data)
        st.success(f"💲 Estimated House Value: ${prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"Error: {e}")

