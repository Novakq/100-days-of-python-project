import requests
import os
from datetime import date, timedelta

os.chdir("Day-36")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
ALPHA_API_KEY ="Q72Q8QN3XXXXX"
ALPHA_API_URL = "https://www.alphavantage.co/query"
ALPHA_FUNCTION = "TIME_SERIES_DAILY"
alpha_api_parameters = {
    "function": ALPHA_FUNCTION,
    "symbol": STOCK,
    "apikey": ALPHA_API_KEY
}


r = requests.get(ALPHA_API_URL,params=alpha_api_parameters)
time_series_data = r.json()

yesterday = date.today() - timedelta(days=1)
day_before_yesterday = date.today() - timedelta(days=2)


data_for_yesterday = float(time_series_data['Time Series (Daily)'][yesterday.strftime('%Y-%m-%d')]['4. close'])
data_for_day_before_yesterday = float(time_series_data['Time Series (Daily)'][day_before_yesterday.strftime('%Y-%m-%d')]['4. close'])

stock_percentage_change = abs((data_for_yesterday-data_for_day_before_yesterday)/data_for_day_before_yesterday)

stock_percentage_change = 0.51
    

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
NEWS_API_KEY = "bf07259151bd4922XXXXXX"
NEWS_API_URL = "https://newsapi.org/v2/everything"
news_api_parameters = {
    "q":COMPANY_NAME,
    "from": yesterday.strftime('%Y-%m-%d'),
    "sortBy":"popularity",
    "apiKey":NEWS_API_KEY,
    "pageSize":3
}


if stock_percentage_change > 0.05:
    r = requests.get(NEWS_API_URL,params=news_api_parameters)
    news_data = r.json()
    print(news_data)

    
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

from twilio.rest import Client 
 
account_sid = 'AC3789ddf2950912ddb4ecfXXXXXX' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(         
                              to='+48XXXX' 
                          ) 
 
print(message.sid)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


