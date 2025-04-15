from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('model/rain_predictor_pipeline.pkl')
print(model.named_steps['preprocessor'].transformers)

app = FastAPI(title="Rain Prediction API")

# Define input schema
class WeatherInput(BaseModel):
    avg_temperature: float
    humidity: float
    pressure: float
    month: int
    day: int
    weekday: int
    avg_wind_speed: float
    cloud_cover: float

# Binning logic (same as your training setup)
def preprocess_input(data):
    wind_speed_bin = pd.cut(
        [data.avg_wind_speed],
        bins=[0, 5, 10, 15, 20, float('inf')],
        labels=[0, 1, 2, 3, 4]
    )[0]

    cloud_cover_bin = pd.cut(
        [data.cloud_cover],
        bins=[0, 25, 50, 75, 100],
        labels=[0, 1, 2, 3]
    )[0]

    return pd.DataFrame([{
        "avg_temperature": data.avg_temperature,
        "humidity": data.humidity,
        "pressure": data.pressure,
        "month": data.month,
        "day": data.day,
        "weekday": data.weekday,
        "wind_speed_bin": wind_speed_bin,
        "cloud_cover_bin": cloud_cover_bin
    }])

@app.post("/predict")
def predict_rain(input_data: WeatherInput):
    df = preprocess_input(input_data)
    prediction = model.predict(df)[0]
    probabilities = model.predict_proba(df)[0]  # Get probabilities for both classes

    return {
        "prediction": int(prediction),
        "meaning": "Rain" if prediction == 1 else "No Rain",
        "probability": {
            "no_rain": round(float(probabilities[0]), 4),
            "rain": round(float(probabilities[1]), 4)
        }
    }