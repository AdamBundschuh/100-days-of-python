from bs4 import BeautifulSoup
import requests
import smtplib
from Passwords import authentication as auth
from email.message import EmailMessage


AUTH = auth.amazon_price_tracker['smtp']
MY_EMAIL = AUTH['my_email']
PASSWORD = AUTH['password']

PRODUCT_URL = "https://www.amazon.com/Sketchboard-Pro-iPad-11-inch-2nd/dp/B093F2S6M1/ref=sr_1_5?crid=2RXSX6A2R94C7&keywords=ipad%2Bboard%2Bfor%2Bdrawing&qid=1701879451&sprefix=ipad%2Bboard%2Caps%2C99&sr=8-5&ufe=app_do%3Aamzn1.fos.18630bbb-fcbb-42f8-9767-857e17e03685&th=1"


response = requests.get(PRODUCT_URL)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
price = int(soup.find("span", class_="a-price-whole").get_text().strip("."))

if price < 200:
    print("Sending email.")
    msg = EmailMessage()
    msg['Subject'] = "Amazon Low Price Alert"
    msg['From'] = MY_EMAIL
    msg['To'] = MY_EMAIL
    msg.set_content(f"Sketchboard is only ${price}")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.send_message(msg)
        connection.quit()
