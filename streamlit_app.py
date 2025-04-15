import streamlit as st
import requests

st.set_page_config(page_title="🌧️ Rain Prediction App", page_icon="🌦️", layout="centered")

# Add a title and description
st.title("🌧️ Will it Rain Today?")
st.markdown(
    """
    Use this app to predict whether it will rain based on weather conditions.
    Adjust the values below and click **Predict** to get your result!
    """,
    unsafe_allow_html=True
)

# Split input fields into two columns
col1, col2 = st.columns(2)

with col1:
    avg_temperature = st.number_input("🌡️ Avg Temperature (°C)", min_value=-50, max_value=60, value=23)
    humidity = st.number_input("💧 Humidity (%)", min_value=0, max_value=100, value=32)
    pressure = st.number_input("🔵 Pressure (hPa)", min_value=800, max_value=1100, value=1013)
    avg_wind_speed = st.number_input("🌬️ Wind Speed (km/h)", min_value=0, max_value=150, value=24)

with col2:
    cloud_cover = st.slider("☁️ Cloud Cover (%)", 0, 100, value=45)
    month = st.selectbox("📅 Month", list(range(1, 13)), index=2)
    day = st.slider("📆 Day", 1, 31, value=3)
    weekday = st.selectbox("🗓️ Weekday (0 = Mon, 6 = Sun)", list(range(7)), index=0)

# Prediction button
if st.button("🔍 Predict"):
    input_data = {
        "avg_temperature": avg_temperature,
        "humidity": humidity,
        "pressure": pressure,
        "month": month,
        "day": day,
        "weekday": weekday,
        "avg_wind_speed": avg_wind_speed,
        "cloud_cover": cloud_cover
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=input_data)
        if response.status_code == 200:
            result = response.json()
            prediction = result["meaning"]
            prob_rain = result["probability"]["rain"]
            prob_no_rain = result["probability"]["no_rain"]

            st.success(f"📢 Prediction: **{prediction}**")
            st.info(f"🔹 Probability of Rain: **{prob_rain * 100:.2f}%**")
            st.info(f"🔹 Probability of No Rain: **{prob_no_rain * 100:.2f}%**")
        else:
            st.error("Failed to get a valid response from the API.")
    except Exception as e:
        st.error(f"Something went wrong: {e}")
