import requests
from twilio.rest import Client

TWILIO_SID = "ACb0247c5c193fc340243231e49bd579f4"
TWILIO_AUTH_TOKEN = "89c2e6a02aaacf9362be3d79329f6b8c"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY = "12757eefd37f41108fd33e26d79c1fd4"
COMPANY_NAME = "Tesla Inc"
STOCK_NAME = "TSLA"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_KEY = "MD50989IM0GF6N33"

NEWS_PARAMS = {
    'apiKey': NEWS_KEY,
    'qInTitle': COMPANY_NAME
}

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
percent_difference = round((price_difference / ((yesterday_price + day_before_price) / 2)) * 1000, 1)
print(percent_difference)


def get_news():
    news_api_result = requests.get(NEWS_ENDPOINT, NEWS_PARAMS)
    news_api_result.raise_for_status()
    three_articles = news_api_result.json()["articles"][:3]
    arrow = '⬆️' if yesterday_price > day_before_price else '⬇️'

    formatted_articles = [f"{STOCK_NAME} {arrow}{percent_difference}%\n*Headline*: {article['title']} \n*Brief*: {article['description']}" for article in three_articles]

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
