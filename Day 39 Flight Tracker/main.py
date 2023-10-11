from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()

# print("Welcome to Flight Club")
# f_name = input("What is your first name? ").title()
# l_name = input("What is your last name? ").title()
# email1 = input("What is your email address? ")
# email2 = input("Please verify your email: ")
#
# while email1 != email2:
#     print("Emails do not match, please try again.")
#     email1 = input("What is your email address? ")
#     email2 = input("Please verify your email: ")
#
# data_manager.add_user(f_name, l_name, email1)


dest_data = data_manager.destination_data
user_data = data_manager.user_data

for row in dest_data:
    if row['iataCode'] == '':
        row['iataCode'] = flight_search.get_destination_code(row['city'])
        data_manager.update_single_destination_code(row)
        print(f"IATA Code updated for {row['iataCode']}")
    else:
        print(f"Code already exists for {row['iataCode']}")

    flight_data = flight_search.get_flight_data(row['iataCode'], row['lowestPrice'])
    if flight_data is not None:
        notification_manager.send_email(flight_data, user_data)
    else:
        print("No flight data found")

