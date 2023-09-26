import requests

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
