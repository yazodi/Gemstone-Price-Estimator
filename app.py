import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title("💎 Gemstone Price Estimator")
st.write("Bu uygulama, değerli taşların fiyatını tahmin eder.")

# Giriş alanları
carat = st.slider("Carat", 0.2, 5.0, 1.0)
depth = st.slider("Depth", 50.0, 70.0, 60.0)
table = st.slider("Table", 50.0, 70.0, 58.0)
x = st.slider("x (mm)", 3.0, 10.0, 6.0)
y = st.slider("y (mm)", 3.0, 10.0, 6.0)
z = st.slider("z (mm)", 2.0, 6.0, 4.0)
clarity_score = st.slider("Clarity Score", 1, 10, 5)
color_score = st.slider("Color Score", 1, 7, 3)
cut_score = st.slider("Cut Score", 1, 5, 3)

# Veriyi dataframe yap
user_input = pd.DataFrame([{
    "carat": carat,
    "depth": depth,
    "table": table,
    "x": x,
    "y": y,
    "z": z,
    "clarity_score": clarity_score,
    "color_score": color_score,
    "cut_score": cut_score
}])

# Model ve kolonlar yükleniyor
model = joblib.load("rf_model.pkl")
columns = joblib.load("model_columns.pkl")

# Sıra uyumu
user_input = user_input[columns]

# Tahmin
if st.button("Tahmini Fiyatı Göster"):
    prediction = model.predict(user_input)[0]
    st.success(f"💰 Tahmini Fiyat: ${prediction:,.2f}")
