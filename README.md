# 🌦️ Weather Prediction System

This is a machine learning-powered weather prediction system that forecasts the likelihood of **rain** based on various meteorological features. It includes:

- 🚀 A FastAPI backend for serving predictions  
- 🎯 A Streamlit frontend for a simple user interface  
- 🧠 A trained XGBoost model integrated into a scikit-learn pipeline  
- 🔍 Probability output for rain and no-rain predictions

---

## 📊 Features

- **Input Parameters**:
  - Average Temperature
  - Humidity
  - Pressure
  - Month, Day, Weekday
  - Average Wind Speed
  - Cloud Cover

- **Model**:
  - `XGBoost` classifier trained using a preprocessing pipeline
  - Outputs a binary prediction (`Rain` / `No Rain`)
  - Returns confidence probabilities for each class

- **Frontend**:
  - Built with Streamlit
  - User-friendly number inputs
  - Displays predicted label and confidence

---

## 🛠 Installation

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/weather-prediction-system.git
cd weather-prediction-system
```

### 2. Create the virtual environment
```bash
python -m venv venv
source venv/bin/activate  # on Unix/macOS
venv\Scripts\activate     # on Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🔌 Backend (FastAPI)

Run the FastAPI server:

```bash
uvicorn api:app --reload
```

## 🌐 Frontend (Streamlit)
```bash
streamlit run streamlit_app.py
```

## 🧠 Model Info

- **Preprocessing**: ColumnTransformer using `OneHotEncoder`, `FunctionTransformer`
- **Classifier**: XGBoost with hyperparameter tuning

### 🔧 Trained with:
- `scikit-learn==1.6.1`
- `xgboost==2.1.4`

> ⚠️ **Note**: Make sure to use compatible versions for model loading to avoid errors during inference.




