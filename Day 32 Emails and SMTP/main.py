import smtplib
import datetime as dt
from random import randint
import pandas

my_email = "email@email.com"
password = "pass1234"
bday_data = pandas.read_csv("birthdays.csv")
now = dt.datetime.now()
now_tuple = (now.month, now.day)

bday_dict = [row for (index, row) in bday_data.iterrows() if (row["month"], row["day"]) == now_tuple]
if bday_dict:  # if list is not empty
    for bday in bday_dict:
        with open(f'./letter_templates/letter_{randint(1, 3)}.txt', 'r') as template_data:
            email_body = template_data.read().replace("[NAME]", bday["name"])
        email_recipient = bday["email"]

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email_recipient,
                msg=f"Subject: Happy Birthday!\n\n{email_body}"
            )
