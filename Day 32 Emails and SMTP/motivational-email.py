import smtplib
import datetime as dt
from random import choice

my_email = "emai@email.com"
password = "pass1234"
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt", "r") as quotes_data:
        all_quotes = quotes_data.readlines()

    with open("emails.txt", "r") as email_data:
        recipients = email_data.read().splitlines()

    for recipient in recipients:
        rand_quote = choice(all_quotes)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=recipient,
                msg=f"Subject:Monday Motivation\n\n{rand_quote}"
            )
