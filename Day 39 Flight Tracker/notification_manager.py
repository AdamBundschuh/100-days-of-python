from flight_data import FlightData
from twilio.rest import Client
import smtplib
from Passwords import authentication as auth
from email.message import EmailMessage

WHATSAPP_AUTH = auth.flight_search['whatsapp']
ACCOUNT_SID = WHATSAPP_AUTH['account_sid']
AUTH_TOKEN = WHATSAPP_AUTH['auth_token']
TO_WHATSAPP = WHATSAPP_AUTH['to_whatsapp']
FROM_WHATSAPP = WHATSAPP_AUTH['from_whatsapp']
WHATSAPP_CLIENT = Client(ACCOUNT_SID, AUTH_TOKEN)
SMTP_AUTH = auth.flight_search['smtp']
FROM_EMAIL = SMTP_AUTH['from_email']
SMTP_PASSWORD = SMTP_AUTH['password']
SMTP_SERVER = SMTP_AUTH['smtp_server']


class NotificationManager:

    def send_whatsapp_message(self, flight_data: FlightData):

        formatted_message = f"✈️ *Low Price Alert* ✈️\n" \
                            f"Only ${flight_data.price} to fly from " \
                            f"{flight_data.depart_city}-{flight_data.depart_code} to " \
                            f"{flight_data.dest_city}-{flight_data.dest_code}, " \
                            f"from {flight_data.depart_date} to {flight_data.return_date}"

        if flight_data.via_city is not None:
            layover_message = f". Flight has 1 layover, via {flight_data.via_city}."
            formatted_message += layover_message

        link_message = f"\n🔗: {flight_data.link}"
        formatted_message += link_message

        message = WHATSAPP_CLIENT.messages.create(
            body=formatted_message,
            from_=FROM_WHATSAPP,
            to=TO_WHATSAPP
        )
        print(f"Message Sent for {flight_data.dest_city}")

    def send_email(self, flight_data: FlightData, user_data):

        print("Sending emails.")

        formatted_message = f"🚨 <b>Cheap Flight to {flight_data.dest_city}</b> 🚨<br><br>" \
                            f"Only ${flight_data.price} to fly from " \
                            f"{flight_data.depart_city}-{flight_data.depart_code} to " \
                            f"{flight_data.dest_city}-{flight_data.dest_code}, " \
                            f"from {flight_data.depart_date} to {flight_data.return_date}"

        if flight_data.via_city is not None:
            layover_message = f".<br><br>Flight has 1 layover, via {flight_data.via_city}."
            formatted_message += layover_message

        link_message = f"<br><br><a href='{flight_data.link}'>Book Now!</a>"

        formatted_message += link_message

        for user in user_data:
            content = f"<p>{formatted_message}</p>"

            msg = EmailMessage()
            msg.set_content(content, subtype='html')
            msg['Subject'] = "✈️ LOW PRICE ALERT!"
            msg['From'] = FROM_EMAIL
            msg['To'] = user['email']
            with smtplib.SMTP(SMTP_SERVER, 587) as smtp:
                smtp.starttls()
                smtp.login(FROM_EMAIL, SMTP_PASSWORD)
                smtp.send_message(msg)
