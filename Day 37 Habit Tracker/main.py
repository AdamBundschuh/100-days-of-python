import requests
from datetime import datetime

USERNAME = "adambundschuh"
TOKEN = "adJ83Jfdh2hf2f93fjjk3261g"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": "adJ83Jfdh2hf2f93fjjk3261g",
    "username": "adambundschuh",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create user account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Hour",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)

today = datetime.now().strftime("%Y%m%d")
yesterday = datetime(year=2023, month=9, day=26)

create_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
crate_pixel_params = {
    "date": today,
    "quantity": "3.5",
}

# Create a pixel
response = requests.post(url=create_pixel_endpoint, json=crate_pixel_params, headers=headers)
print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
update_pixel_params = {
    "quantity": "2.75"
}

# Update a pixel
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)