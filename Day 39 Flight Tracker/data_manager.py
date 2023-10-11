import requests
from Passwords import authentication as auth

AUTH = auth.flight_search['sheety']
API_KEY = AUTH['api_key']
ENDPOINT = AUTH['endpoint']
DEST_ENDPOINT = f"{ENDPOINT}/prices"
USER_ENDPOINT = f"{ENDPOINT}/users"

headers = {
    "Authentication": API_KEY,
    "Content-Type": "application/json"
}


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.user_data = {}
        self.get_data()

    def get_data(self):
        response = requests.get(url=DEST_ENDPOINT, headers=headers)
        dest_data = response.json()
        self.destination_data = dest_data["prices"]

        response = requests.get(url=USER_ENDPOINT, headers=headers)
        user_data = response.json()
        self.user_data = user_data["users"]

    def update_all_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{DEST_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def update_single_destination_code(self, destination):

        new_data = {
            "price": {
                "iataCode": destination['iataCode']
            }
        }
        response = requests.put(
            url=f"{DEST_ENDPOINT}/{destination['id']}",
            json=new_data
        )
        print(response.text)

    def add_user(self, f_name, l_name, email):
        print("Adding new user")

        new_user = {
            "user": {
                "firstName": f_name,
                "lastName": l_name,
                "email": email
            }
        }
        response = requests.post(
            url=USER_ENDPOINT,
            json=new_user
        )
        print(response.text)
