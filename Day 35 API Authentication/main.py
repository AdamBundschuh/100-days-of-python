import requests

api_key = "6eb263cbd34d4bfca21180355231206"
base_url = "http://api.weatherapi.com/v1"

API_MAP = {
    'current': '/current.json',
    'forecast': '/forecast.json',
    'search': '/search.json',
    'history': '/history.json',
    'marine': 'marine.json',
    'future': 'future.json',
    'timezone': '/timezone.json',
    'sports': '/sports.json',
    'astronomy': '/astronomy.json',
    'iplookup': '/ip.json',
}

api_url = base_url + API_MAP['forecast']

params = {
    'key': api_key,
    'q': 'Columbus',
    'days': 3
}

api_result = requests.get(api_url, params)
api_result.raise_for_status()
data = api_result.json()


# Current Day
day_1 = data['forecast']['forecastday'][0]
rain_on_day_1 = True if day_1['day']['daily_will_it_rain'] == 1 else False


# Tomorrow
day_2 = data['forecast']['forecastday'][1]
rain_on_day_2 = True if day_2['day']['daily_will_it_rain'] == 1 else False

# Day after tomorrow
day_3 = data['forecast']['forecastday'][2]
rain_on_day_3 = True if day_3['day']['daily_will_it_rain'] == 1 else False

print(f"Will it rain today? {'Yes' if {rain_on_day_1} else 'No'}")
print(f"Will it rain tomorrow? {'Yes' if {rain_on_day_2} else 'No'}")
print(f"Will it rain the day after tomorrow? {'Yes' if {rain_on_day_3} else 'No'}")
