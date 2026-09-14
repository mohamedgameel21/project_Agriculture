# 🌾 Crop Yield Prediction Web App

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Pandas](https://img.shields.io/badge/Pandas-Latest-150458.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

تطبيق ويب تفاعلي ومبسط مُصمم للتنبؤ بإنتاجية المحاصيل الزراعية (بالطن / هكتار) اعتماداً على العوامل المناخية والبيئية ونوع التربة والممارسات الزراعية.

---

## 📌 Features

* **واجهة تفاعلية عبر Streamlit:** تمكّن المستخدم من تعديل المدخلات ورؤية النتائج فوراً.
* **تغطية شاملة للمتغيرات:**
  * **البيانات المكانية والتربة:** المنطقة (`Region`) ونوع التربة (`Soil_Type`).
  * **أنواع المحاصيل:** القطن، الأرز، الشعير، فول الصويا، والقمح.
  * **المناخ والطقس:** درجة الحرارة، معدل الأمطار، وحالة الطقس (`Sunny`, `Rainy`, إلخ).
  * **الممارسات الزراعية:** استخدام الأسمدة، الري، وعدد الأيام حتى الحصاد[cite: 1].
* **تنبؤ فوري:** يعتمد على نموذج تعلم آلة مُدرب مسبقاً (`crop_model.pkl`) ويتم تحميلة باستخدام `joblib`[cite: 1].

---

## 📁 Repository Structure

```text
├── app.py              # Streamlit Web Application interface
├── train_model.py      # Script to train and save the ML model
├── crop_model.pkl      # Trained machine learning model file
├── requirements.txt    # Required Python dependencies
└── README.md           # Project documentation
