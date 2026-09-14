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
```
🚀 Quick Start
1. Prerequisites
Ensure you have Python 3.9+ installed on your system[cite: 1].

2. Installation & Setup
Clone the repository and install the required dependencies:

Bash
# Clone the repository
git clone [https://github.com/your-username/crop-yield-prediction.git](https://github.com/your-username/crop-yield-prediction.git)
cd crop-yield-prediction

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
3. Model Training (Optional)
If crop_model.pkl is missing or if you want to retrain the model on fresh data:

Bash
python train_model.py
4. Running the Web Application
Launch the Streamlit app locally:

Bash
streamlit run app.py
The application will automatically open in your browser at http://localhost:8501[cite: 1].

💻 Tech Stack
Python - Core programming language.

Streamlit - Interactive web deployment framework[cite: 1].

Pandas - Data structures and input manipulation[cite: 1].

Scikit-Learn / Joblib - Machine learning modeling and artifact loading[cite: 1].

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to submit a Pull Request or open an Issue.
