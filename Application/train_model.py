import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"

import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# بيانات وهمية خفيفة للنموذج
dummy_data = pd.DataFrame({
    'Region': ['West', 'South', 'North', 'East'],
    'Soil_Type': ['Sandy', 'Clay', 'Loam', 'Silt'],
    'Crop': ['Cotton', 'Rice', 'Barley', 'Wheat'],
    'Rainfall_mm': [897.0, 992.0, 147.0, 730.0],
    'Temperature_Celsius': [27.6, 18.0, 29.7, 31.6],
    'Fertilizer_Used': [0, 1, 0, 1],
    'Irrigation_Used': [1, 1, 0, 1],
    'Weather_Condition': ['Cloudy', 'Rainy', 'Sunny', 'Clear'],
    'Days_to_Harvest': [90, 120, 110, 100],
    'Yield_tons_per_hectare': [6.5, 8.5, 1.1, 7.2]
})

X = dummy_data.drop('Yield_tons_per_hectare', axis=1)
y = dummy_data['Yield_tons_per_hectare']

cat_cols = ['Region', 'Soil_Type', 'Crop', 'Weather_Condition']
num_cols = ['Rainfall_mm', 'Temperature_Celsius', 'Fertilizer_Used', 'Irrigation_Used', 'Days_to_Harvest']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_cols)
    ]
)

model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

model_pipeline.fit(X, y)
joblib.dump(model_pipeline, 'crop_model.pkl')
print("✅ تم حفظ النموذج بنجاح في crop_model.pkl")