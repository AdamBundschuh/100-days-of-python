import requests
from datetime import datetime, timedelta
from flight_data import FlightData
from Passwords import authentication as auth

AUTH = auth.flight_search['tequila']
API_KEY = AUTH['api_key']
ENDPOINT = "https://api.tequila.kiwi.com"
FROM_IATA_CODE = "CMH"
CURRENCY = "USD"

header = {
    "apikey": API_KEY,
}


class FlightSearch:

    def get_destination_code(self, city_name):

        dest_params = {
            "term": city_name,
            "location_type": "airport"
        }

        response = requests.get(url=f"{ENDPOINT}/locations/query", params=dest_params, headers=header)
        city_code = response.json()['locations'][0]['code']

        return city_code

    def get_flight_data(self, iata_code, max_price):

        from_date = datetime.today()
        to_date = from_date + timedelta(days=180)

        params = {
            "fly_from": FROM_IATA_CODE,
            "fly_to": iata_code,
            "date_from": from_date.strftime("%d/%m/%Y"),
            "date_to": to_date.strftime("%d/%m/%Y"),
            "max_stopovers": '2',
            "nights_in_dst_from": '4',
            "nights_in_dst_to": '14',
            "curr": CURRENCY,
            "price_to": max_price,
            "limit": 1
        }

        response = requests.get(url=f"{ENDPOINT}/search", params=params, headers=header)

        if response.json()['_results'] > 0:
            flight_data = FlightData(response.json()['data'][0])
            return flight_data
