import requests
from Passwords import authentication as auth

AUTH = auth.flight_search['sheety']
API_KEY = AUTH['api_key']
ENDPOINT = "https://api.sheety.co/d072de6e229f2ef33682abecc9cbe9ce/personalFlightDeals/prices"

headers = {
    "Authentication": API_KEY,
    "Content-Type": "application/json"
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_all_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def update_single_destination_code(self, destination):
        print("Updating IATA Code in Google Sheet")

        new_data = {
            "price": {
                "iataCode": destination['iataCode']
            }
        }
        response = requests.put(
            url=f"{ENDPOINT}/{destination['id']}",
            json=new_data
        )
        print(response.text)
