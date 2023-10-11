from datetime import datetime
import requests
import json
from Passwords import authentication as auth

AUTH = auth.flight_search['rebrandly']

KEY = AUTH['api_key']


class FlightData:

    def __init__(self, price, dest_city, dest_code, depart_city, depart_code, route_data, link):
        self.price = price
        self.dest_city = dest_city
        self.dest_code = dest_code
        self.via_city = self.get_layover(route_data)
        self.depart_city = depart_city
        self.depart_code = depart_code
        self.depart_date = self.get_depart_date(route_data)
        self.return_date = self.get_return_date(route_data)
        self.link = self.get_short_link(link)
        # self.img_link = self.get_dest_image(dest_city)

    def get_dest_image(self, dest_city):
        image_url = f"https://api.teleport.org/api/urban_areas/slug:{dest_city}/images/"
        print(f"Image URL: {image_url}")
        requests.get(url=f"https://api.teleport.org/api/urban_areas/slug:{dest_city}/images/")

    def get_depart_date(self, route_data):
        first_route = route_data[0]
        return datetime.fromtimestamp(first_route['dTime']).strftime('%m/%d/%Y')

    def get_return_date(self, route_data):
        last_route = route_data.pop()
        return datetime.fromtimestamp(last_route['aTime']).strftime('%m/%d/%Y')

    def get_layover(self, route_data):
        if len(route_data) > 2:
            print("Layover exists.")
            return route_data[1]['cityFrom']

    def get_short_link(self, long_url):
        # linkRequest = {
        #     "destination": long_url
        #     , "domain": {"fullName": "rebrand.ly"}
        # }
        #
        # requestHeaders = {
        #     "Content-type": "application/json",
        #     "apikey": KEY,
        # }
        #
        # r = requests.post("https://api.rebrandly.com/v1/links",
        #                   data=json.dumps(linkRequest),
        #                   headers=requestHeaders)
        #
        # if (r.status_code == requests.codes.ok):
        #     link = r.json()
        #     return link["shortUrl"]
        # Disabled temporarily due to api usage
        return long_url

