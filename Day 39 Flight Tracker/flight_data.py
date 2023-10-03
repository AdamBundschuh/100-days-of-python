from datetime import datetime
import requests
from pprint import pprint
import json

KEY = 'a5f69cad61c242beaead4ce02a0b89bd'


class FlightData:

    def __init__(self, flight_data):
        self.dest_city = flight_data['cityTo']
        self.dest_code = flight_data['cityCodeTo']
        self.price = flight_data['price']
        self.depart_city = flight_data['cityFrom']
        self.depart_code = flight_data['cityCodeFrom']
        self.depart_date = self.get_depart_date(flight_data)
        self.return_date = self.get_return_date(flight_data)
        self.link = self.get_short_link(flight_data['deep_link'])

    def get_depart_date(self, flight_data):
        first_route = flight_data['route'][0]
        return datetime.fromtimestamp(first_route['dTime']).strftime('%m/%d/%Y')

    def get_return_date(self, flight_data):
        last_route = flight_data['route'].pop()
        return datetime.fromtimestamp(last_route['aTime']).strftime('%m/%d/%Y')

    def get_short_link(self, long_url):
        linkRequest = {
            "destination": long_url
            , "domain": {"fullName": "rebrand.ly"}
        }

        requestHeaders = {
            "Content-type": "application/json",
            "apikey": KEY,
        }

        r = requests.post("https://api.rebrandly.com/v1/links",
                          data=json.dumps(linkRequest),
                          headers=requestHeaders)

        if (r.status_code == requests.codes.ok):
            link = r.json()
            # print("Long URL was %s, short URL is %s" % (link["destination"], link["shortUrl"]))
            return link["shortUrl"]
