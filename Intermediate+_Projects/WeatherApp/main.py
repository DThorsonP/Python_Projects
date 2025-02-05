import requests
from twilio.rest import Client

account_sid = "AC2791a27f0ee304a8662a03ab0e3f961f"
auth_token = "87059bbab84fb1ec1d21568e9b2c9ec1"
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "06bceed6ec53871ab630e28a834b0ace"

weather_params = {
    "lat": 38.252666,
    "lon": -85.758453,
    "cnt": 4,
    "appid": api_key,
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
       will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='MGbe67c256cea3edf946a583d54bbb6ba9',
        to="whatsapp:+18887776409",
        from_="whatsapp:+14155238886",
        body="It's going to rain so bring an umbrella ☔️ ",

    )
    print(message.status)
