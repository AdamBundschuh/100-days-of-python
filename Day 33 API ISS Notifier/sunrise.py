import requests
from datetime import datetime as dt

MY_LAT = 39.962760
MY_LONG = -82.996290

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise_hour = data["results"]["sunrise"]
sunset_hour = data["results"]["sunset"]
print(f"Sunset hour: {sunset_hour}")
print(f"Sunrise hour: {sunrise_hour}")


time_now = dt.now()
print(f"Time now hour: {time_now.hour}")




