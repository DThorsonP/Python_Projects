import requests
# Test API call for Open Weather API key
# https://api.openweathermap.org/data/2.5/weather?q=London,UK&appid=06bceed6ec53871ab630e28a834b0ace

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "06bceed6ec53871ab630e28a834b0ace"

weather_params = {
    "lat": 30.267153,
    "lon": -97.743057,
    "cnt": 4,
    "appid": api_key,
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_codce = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
       will_rain = True
if will_rain:
    print("Bring an ☂️")
    