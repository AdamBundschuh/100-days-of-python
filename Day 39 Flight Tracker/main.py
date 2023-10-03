from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

# sheet_data = [
#   {"city": "Paris", "iataCode": "", "id": 2, "lowestPrice": 60},
#   {"city": "Berlin", "iataCode": "", "id": 3, "lowestPrice": 42},
#   {"city": "Tokyo", "iataCode": "", "id": 4, "lowestPrice": 485},
#   {"city": "Sydney", "iataCode": "", "id": 5, "lowestPrice": 551},
#   {"city": "Istanbul", "iataCode": "", "id": 6, "lowestPrice": 95},
#   {"city": "Kuala Lumpur", "iataCode": "", "id": 7, "lowestPrice": 414},
#   {"city": "New York", "iataCode": "", "id": 8, "lowestPrice": 240},
#   {"city": "San Francisco", "iataCode": "", "id": 9, "lowestPrice": 260},
#   {"city": "Cape Town", "iataCode": "", "id": 10, "lowestPrice": 378}
# ]

for row in sheet_data:
    if row['iataCode'] == '':
        row['iataCode'] = flight_search.get_destination_code(row['city'])
        data_manager.update_single_destination_codes(row)

    flight_data = flight_search.get_flight_data(row['iataCode'], row['lowestPrice'])
    if flight_data is not None:
        notification_manager.send_sms_message(flight_data)



