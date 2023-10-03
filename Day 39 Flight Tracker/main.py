from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

for row in sheet_data:
    if row['iataCode'] == '':
        row['iataCode'] = flight_search.get_destination_code(row['city'])
        data_manager.update_single_destination_code(row)

    flight_data = flight_search.get_flight_data(row['iataCode'], row['lowestPrice'])
    if flight_data is not None:
        notification_manager.send_sms_message(flight_data)



