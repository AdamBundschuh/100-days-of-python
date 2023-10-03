from flight_data import FlightData
from twilio.rest import Client

ACCOUNT_SID = 'ACb0247c5c193fc340243231e49bd579f4'
AUTH_TOKEN = 'd63c1401ce3b6e9e1fba342135cc2e79'
TO_WHATSAPP = 'whatsapp:+14193410548'
FROM_WHATSAPP = 'whatsapp:+14155238886'
client = Client(ACCOUNT_SID, AUTH_TOKEN)


class NotificationManager:

    def send_sms_message(self, flight_data: FlightData):
        formatted_message = f"✈️ *Low Price Alert* ✈️\n" \
                            f"Only ${flight_data.price} to fly from " \
                            f"{flight_data.depart_city}-{flight_data.depart_code} to " \
                            f"{flight_data.dest_city}-{flight_data.dest_code}, " \
                            f"from {flight_data.depart_date} to {flight_data.return_date}\n" \
                            f"🔗: {flight_data.link}"

        message = client.messages.create(
            body=formatted_message,
            from_=FROM_WHATSAPP,
            to=TO_WHATSAPP
        )
        print(f"Message Sent: {message}")
