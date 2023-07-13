import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv
import datetime

load_dotenv()

# Constants and env
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
RECIPIENT_PHONE_NUMBER = os.getenv("RECIPIENT_PHONE_NUMBER")


stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_VANTAGE_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)

json_response = response.json()

fecha_actual = datetime.datetime.now()
fecha_ayer = fecha_actual - datetime.timedelta(days=1)
fecha_ayer_formateada = fecha_ayer.strftime("%Y-%m-%d")
fecha_antier = fecha_actual - datetime.timedelta(days=2)
fecha_antier_formateada = fecha_antier.strftime("%Y-%m-%d")

acciones_ayer_al_cierre = float(json_response["Time Series (Daily)"][fecha_ayer_formateada]['4. close'])
acciones_antier_al_cierre = float(json_response["Time Series (Daily)"][fecha_antier_formateada]['4. close'])


diferencia = acciones_antier_al_cierre - acciones_ayer_al_cierre
if diferencia >= 0:
    ganancia = "↑"
else:
    ganancia = "↓"
diferencia = abs(diferencia)

porcentaje_diferencia = (diferencia / acciones_antier_al_cierre) * 100

# if porcentaje_diferencia > 5:
if True:
    url = 'https://newsapi.org/v2/everything'
    params_news = {
        "q": COMPANY_NAME,
        "pageSize": 3,
        "apiKey": NEWS_API_KEY,
        }
    response = requests.get(url, params=params_news)
    articles = response.json()['articles']
    titles = []
    description = []
    titles = [json_obj['title'] for json_obj in articles if 'title' in json_obj]
    description = [json_obj['description'] for json_obj in articles if 'description' in json_obj]
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for i in range(len(titles)):
        message = client.messages.create(
        from_=TWILIO_PHONE_NUMBER,
        body=f'{STOCK_NAME}: {ganancia} {diferencia} % Headline: {titles[i]}. Brief: {description[i]}',
        to=RECIPIENT_PHONE_NUMBER
        )
        print(message.sid)
