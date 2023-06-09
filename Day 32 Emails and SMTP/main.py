import smtplib
import datetime as dt
from random import choice

my_email = "hdocpython@gmail.com"
password = "epdjzoprcudardol"
recipient_email = "ehottinger@gmail.com"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    date_str = now.strftime('%D')
    subj_txt = f"Motivation Monday for {date_str}"

    with open("quotes.txt", "r") as data:
        all_quotes = data.readlines()
        rand_quote = choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg=f"Subject:{subj_txt}\n\n{rand_quote}"
        )
