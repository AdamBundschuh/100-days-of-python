from flight_data import FlightData
from twilio.rest import Client
from Passwords import authentication as auth

AUTH = auth.flight_search['whatsapp']
ACCOUNT_SID = AUTH['account_sid']
AUTH_TOKEN = AUTH['auth_token']
TO_WHATSAPP = AUTH['to_whatsapp']
FROM_WHATSAPP = AUTH['from_whatsapp']

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
        print(f"Message Sent for {flight_data.dest_city}")
