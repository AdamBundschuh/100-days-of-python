import requests
from twilio.rest import Client

TWILIO_SID = "ACb0247c5c193fc340243231e49bd579f4"
TWILIO_AUTH_TOKEN = "89c2e6a02aaacf9362be3d79329f6b8c"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY = "12757eefd37f41108fd33e26d79c1fd4"
COMPANY_NAME = "Tesla Inc"

NEWS_PARAMS = {
    'apiKey': NEWS_KEY,
    'qInTitle': COMPANY_NAME
}

STOCK_NAME = "TSLA"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_KEY = "MD50989IM0GF6N33"

STOCK_PARAMS = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'outputsize': 'compact',
    'datatype': 'json',
    'apikey': STOCK_KEY,
}

stock_api_result = requests.get(STOCK_ENDPOINT, STOCK_PARAMS)
stock_api_result.raise_for_status()
stock_data = stock_api_result.json()

daily_stocks = stock_data['Time Series (Daily)']
daily_stocks_list = [value for (key, value) in daily_stocks.items()]

yesterday = daily_stocks_list[0]
yesterday_price = float(yesterday['4. close'])

day_before = daily_stocks_list[1]
day_before_price = float(day_before['4. close'])

price_difference = round(abs(yesterday_price - day_before_price), 2)
percent_difference = (price_difference / ((yesterday_price + day_before_price) / 2)) * 1000
print(percent_difference)


def get_news():
    news_api_result = requests.get(NEWS_ENDPOINT, NEWS_PARAMS)
    news_api_result.raise_for_status()
    three_articles = news_api_result.json()["articles"][:3]
    arrow = '⬆️' if yesterday_price > day_before_price else '⬇️'

    formatted_articles = [f"{STOCK_NAME} {arrow}{round(percent_difference,1)}%\n*Headline*: {article['title']} \n*Brief*: {article['description']}" for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    to_whatsapp = '+14193410548'

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='whatsapp:+14155238886',
            to=to_whatsapp
        )
        print(message.sid)


if percent_difference >= .5:
    get_news()


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
