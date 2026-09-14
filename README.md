# 🌾 Crop Yield Prediction Web App

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Pandas](https://img.shields.io/badge/Pandas-Latest-150458.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

An interactive web application designed to predict agricultural crop yield (in Tons per Hectare) based on climatic conditions, soil types, environmental factors, and farming practices.

---

## 📌 Features

* **Interactive Interface:** Built with Streamlit to allow real-time parameter tuning and instant yield predictions.
* **Comprehensive Feature Inputs:**
  * **Geographical & Soil Data:** Region selection (`Region`) and soil classification (`Soil_Type`).
  * **Crop Diversity:** Support for Cotton, Rice, Barley, Soybean, and Wheat.
  * **Climatic Parameters:** Temperature, rainfall levels, and general weather condition (`Sunny`, `Rainy`, etc.).
  * **Farming Practices:** Fertilizer application, irrigation usage, and days to harvest[cite: 1].
* **Instant Inference:** Utilizes a pre-trained machine learning model (`crop_model.pkl`) loaded efficiently using `joblib`[cite: 1].

---

## 📁 Repository Structure

```text
├── app.py              # Streamlit Web Application interface
├── train_model.py      # Script to train and save the ML model
├── crop_model.pkl      # Trained machine learning model file
├── requirements.txt    # Required Python dependencies
└── README.md           # Project documentation
