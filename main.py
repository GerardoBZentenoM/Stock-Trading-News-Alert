import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv
import json 
import datetime 

# Load environment variables from .env file
load_dotenv()

# Constants
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHA_VANTAGE_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
RECIPIENT_PHONE_NUMBER = os.getenv("RECIPIENT_PHONE_NUMBER")


## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Step 1: Get yesterday's and day before yesterday's closing stock prices
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_VANTAGE_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)

json_response = response.json()
print(json_response)

fecha_actual = datetime.datetime.now()

fecha_ayer = fecha_actual - datetime.timedelta(days=1)
fecha_ayer_formateada = fecha_ayer.strftime("%Y-%m-%d")

fecha_antier = fecha_actual - datetime.timedelta(days=2)
fecha_antier_formateada = fecha_antier.strftime("%Y-%m-%d")

print("Fecha de ayer:", fecha_ayer_formateada)
print("Fecha de antier:", fecha_antier_formateada)

acciones_ayer_al_cierre = float(json_response["Time Series (Daily)"][fecha_ayer_formateada]['4. close'])
acciones_antier_al_cierre = float(json_response["Time Series (Daily)"][fecha_antier_formateada]['4. close'])



#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
print("acciones_ayer:", acciones_ayer_al_cierre)

#TODO 2. - Get the day before yesterday's closing stock price
print("acciones_antier:", acciones_antier_al_cierre)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diferencia = acciones_antier_al_cierre - acciones_ayer_al_cierre
print(diferencia)
if diferencia >= 0:
    ganancia = True
else:    
    ganancia = False
print("Diferencia", abs(diferencia))

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
porcentaje_diferencia = (diferencia / acciones_antier_al_cierre) * 100

# Imprimir el porcentaje de diferencia
print("El porcentaje de diferencia es:", porcentaje_diferencia, "%")
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if porcentaje_diferencia > 5:
    print("Get News")
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

