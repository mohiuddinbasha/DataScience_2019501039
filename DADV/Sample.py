import requests
from bs4 import BeautifulSoup
import io
import pandas as pd
import datetime

url = "https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=1519842600&period2=1544639400&interval=1d&events=history&includeAdjustedClose=true"

response = requests.get(url)
bytes_io = io.BytesIO(response.content)
df = pd.read_csv(bytes_io)
df['Symbol'] = 'AAPL'
