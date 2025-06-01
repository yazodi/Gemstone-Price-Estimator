---
title: "💎 Gemstone Price Regression"
emoji: 💰
colorFrom: indigo
colorTo: blue
sdk: streamlit
app_file: app.py
pinned: true
license: mit
tags:
  - regression
  - machine-learning
  - streamlit
  - diamonds
  - synthetic-data
---

# 💎 Gemstone Price Prediction App

This Streamlit app predicts the price of a gemstone using its physical and quality-related features.

## 🧠 Project Overview

- This project simulates a **gemstone pricing system** using synthetic tabular data.
- Features include: `carat`, `depth`, `table`, `x`, `y`, `z`, `clarity_score`, `color_score`, and `cut_score`.
- The target variable is **price** (USD).
- Model: **RandomForestRegressor**
- Trained on 1000 synthetic samples.

---

## 📊 Performance

- RMSE: **605.16**
- R² Score: **0.9549**

---

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py



🔮 Future Work
Area	Improvement
Model	Try XGBoost, LightGBM
Feature Engineering	Interaction terms, log/carat scaling
Deployment	Add API endpoint with FastAPI
Real-world Data	Integrate real gemstone datasets


📁 Files
app.py: Streamlit interface

rf_model.pkl: Trained model

model_columns.pkl: List of input features

requirements.txt: Required libraries

