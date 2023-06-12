import requests

# https://api.openweathermap.org/data/2.5/weather?q=Columbus&appid=2161ad81a45a6b79110301dfd70c17ca
api_key = "2161ad81a45a6b79110301dfd70c17ca"
city = "Columbus"

params = {
    'lat': 39.961141,
    'lon': -83.013059,
    'exclude': "current,minutely",
    'appid': api_key,

}

api_result = requests.get('https://api.openweathermap.org/data/2.5/onecall', params)

api_response = api_result.json()

print(api_response)
