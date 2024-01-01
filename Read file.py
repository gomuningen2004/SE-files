import pandas as pd

def weather_predictor(T, H, w):
    W = (0.5 * (T**2)) - (0.2 * H) + (0.1 * w) - 15
    if W > 300:
        return "Sunny"
    elif 200 < W <= 300:
        return "Cloudy"
    elif 100 < W <= 200:
        return "Rainy"
    else:
        return "Stormy"

file_path = "weather_values.xlsx"
df = pd.read_excel(file_path)
for index, row in df.iterrows():
    t = row['Temperature']
    h = row['Humidity']
    ws = row['Wind speed']
    print(f"The weather condition for temperature : {t}, humidity : {h}, and wind speed : {ws} is {weather_predictor(t, h, ws)}")
