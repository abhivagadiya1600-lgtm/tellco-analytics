import warnings
warnings.filterwarnings('ignore', category=UserWarning)

import streamlit as st # type: ignore
import pandas as pd
import joblib

st.set_page_config(page_title="Rossmann Sales Predictor", layout="centered")

st.title("Rossmann Store Sales Forecasting")
st.write("Predict daily sales based on store characteristics and promotional events.")

# Load trained pipeline
@st.cache_resource
def load_model():
    return joblib.load('model-29-07-2026-10-52-13-00.pkl')

model = load_model()

st.sidebar.header("Store Features")
store_id = st.sidebar.number_input("Store ID", min_value=1, max_value=1115, value=1)
day_of_week = st.sidebar.slider("Day of Week (1=Mon, 7=Sun)", 1, 7, 1)
promo = st.sidebar.selectbox("Is Promo Active?", [0, 1])
school_holiday = st.sidebar.selectbox("School Holiday?", [0, 1])
state_holiday = st.sidebar.selectbox("State Holiday", ["None", "Public Holiday", "Easter", "Christmas"])
comp_dist = st.sidebar.number_input("Competition Distance (meters)", min_value=0, value=1000)

mapping = {"None": 0, "Public Holiday": 1, "Easter": 2, "Christmas": 3}
state_holiday_val = mapping[state_holiday]

if st.button("Predict Sales"):
    input_data = pd.DataFrame([{
        'Store': store_id,
        'DayOfWeek': day_of_week,
        'Promo': promo,
        'StateHoliday': state_holiday_val,
        'SchoolHoliday': school_holiday,
        'StoreType': 1,
        'Assortment': 1,
        'CompetitionDistance': comp_dist,
        'Year': 2026,
        'Month': 7,
        'Day': 28,
        'WeekOfYear': 31,
        'IsWeekend': 1 if day_of_week in [6, 7] else 0
    }])
    
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Daily Sales: **${prediction:,.2f}**")
    