import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"

import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="تطبيق التنبؤ بإنتاجية المحاصيل", page_icon="🌾", layout="wide")

st.title("🌾 نظام التنبؤ بإنتاجية المحاصيل (Crop Yield Prediction)")

@st.cache_resource
def load_model():
    return joblib.load('crop_model.pkl')

try:
    model = load_model()
except Exception as e:
    st.error("لم يتم العثور على ملف النموذج `crop_model.pkl`. يرجى تشغيل train_model.py أولاً.")
    st.stop()

# القائمة الجانبية
st.sidebar.header("📋 إدخال البيانات الزراعية")

region = st.sidebar.selectbox("المنطقة:", ['West', 'South', 'North', 'East'])
soil_type = st.sidebar.selectbox("نوع التربة:", ['Sandy', 'Clay', 'Loam', 'Silt'])
crop = st.sidebar.selectbox("المحصول:", ['Cotton', 'Rice', 'Barley', 'Soybean', 'Wheat'])
weather = st.sidebar.selectbox("حالة الطقس:", ['Cloudy', 'Rainy', 'Sunny', 'Clear'])

rainfall = st.sidebar.slider("معدل الأمطار (mm):", 100.0, 1000.0, 550.0)
temperature = st.sidebar.slider("درجة الحرارة (C):", 15.0, 40.0, 27.5)
days_to_harvest = st.sidebar.slider("عدد الأيام حتى الحصاد:", 60, 150, 100)

fertilizer_used = st.sidebar.radio("استخدام أسمدة؟", ["نعم", "لا"])
irrigation_used = st.sidebar.radio("استخدام الري؟", ["نعم", "لا"])

input_df = pd.DataFrame([{
    'Region': region,
    'Soil_Type': soil_type,
    'Crop': crop,
    'Rainfall_mm': rainfall,
    'Temperature_Celsius': temperature,
    'Fertilizer_Used': 1 if fertilizer_used == "نعم" else 0,
    'Irrigation_Used': 1 if irrigation_used == "نعم" else 0,
    'Weather_Condition': weather,
    'Days_to_Harvest': days_to_harvest
}])

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 البيانات المدخلة:")
    st.dataframe(input_df, use_container_width=True)

with col2:
    st.subheader("📈 التنبؤ بالإنتاجية:")
    if st.button("حساب الإنتاجية المتوقعة 🚀", use_container_width=True):
        prediction = model.predict(input_df)[0]
        st.success("**الإنتاجية المتوقعة:**")
        st.metric(label="طن / هكتار", value=f"{max(0.0, float(prediction)):.2f}")