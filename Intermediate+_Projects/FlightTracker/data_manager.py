import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

DATA_ENDPOINT = "https://api.sheety.co/1e7e4531c29943f562063f1cff9b8c9a/flightDeals/sheet1"

class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USRERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=DATA_ENDPOINT, auth=self._authorization)
        data = response.json()
        self.destination_data = data["sheet1"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "sheet1": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{DATA_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=self._authorization
            )
            print(response.text)
