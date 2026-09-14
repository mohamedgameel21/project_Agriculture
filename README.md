# 🌾 Crop Yield Prediction Web App

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Pandas](https://img.shields.io/badge/Pandas-Latest-150458.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

An interactive web application built with Streamlit designed to predict agricultural crop yield (in Tons per Hectare) based on climatic conditions, soil types, environmental parameters, and farming practices.

---

## 📌 Features

* **Interactive User Interface:** Built with Streamlit to allow real-time parameter tuning and instant yield prediction calculation.
* **Comprehensive Parameter Coverage:**
  * **Geographical & Soil Features:** Region selection (`West`, `South`, `North`, `East`) and soil classification (`Sandy`, `Clay`, `Loam`, `Silt`).
  * **Crop Diversity:** Predictions tailored for Cotton, Rice, Barley, Soybean, and Wheat.
  * **Climatic Parameters:** Temperature, rainfall levels (mm), and weather condition (`Cloudy`, `Rainy`, `Sunny`, `Clear`).
  * **Farming Practices:** Fertilizer and irrigation usage toggles, along with days to harvest[cite: 1].
* **Fast & Efficient Inference:** Loads a pre-trained machine learning model (`crop_model.pkl`) using `joblib` resource caching for quick predictions[cite: 1].

---

## 📁 Repository Structure

```text
├── app.py              # Streamlit Web Application interface
├── train_model.py      # Script to train and save the ML model
├── crop_model.pkl      # Pre-trained machine learning model artifact
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
