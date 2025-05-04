# Import the required libraries namely requests, BeautifulSoup ,pandas, openpyxl
import requests
from bs4 import BeautifulSoup
import time
import psutil
import pandas as pd

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

urls = [
    'https://www.investing.com/equities/nike',
    'https://www.investing.com/equities/coca-cola-co',
    'https://www.investing.com/equities/microsoft-corp',
    'https://www.investing.com/equities/3m-co',
    'https://www.investing.com/equities/american-express',
    'https://www.investing.com/equities/amgen-inc',
    'https://www.investing.com/equities/apple-computer-inc',
    'https://www.investing.com/equities/boeing-co',
    'https://www.investing.com/equities/cisco-sys-inc',
    'https://www.investing.com/equities/goldman-sachs-group',
    'https://www.investing.com/equities/ibm',
    'https://www.investing.com/equities/intel-corp',
    'https://www.investing.com/equities/jp-morgan-chase',
    'https://www.investing.com/equities/mcdonalds',
    'https://www.investing.com/equities/salesforce-com',
    'https://www.investing.com/equities/verizon-communications',
    'https://www.investing.com/equities/visa-inc',
    'https://www.investing.com/equities/wal-mart-stores',
    'https://www.investing.com/equities/disney'
    ]

# Parse the html data and retrieve the required data from the HTML page and store it
all=[]
for url in urls:
    page = requests.get(url,headers=headers)

    try:

        soup = BeautifulSoup(page.text,'html.parser')
        
        # Retrieve the company name from the HTML source
        company = soup.find('h1', {'class':'text-2xl font-semibold instrument-header_title__gCaMF mobile:mb-2'}).text


        # Retrieve the price of the stock from the HTML source
        price = soup.find('div', {'class':'instrument-price_instrument-price__xfgbB flex items-end flex-wrap font-bold'}).find_all('span')[0].text


        # Retrieve the change percentage of price of the stock from the HTML source
        change = soup.find('div', {'class':'instrument-price_instrument-price__xfgbB flex items-end flex-wrap font-bold'}).find_all('span')[2].text

        # Retrieve the volume of the stock from the HTML source
        volume = soup.find('div',{'class':'trading-hours_value__5_NnB'}).text

        x = [company,price,change,volume]
        all.append(x)
        print(x)

    except AttributeError:
        print("Change the Element id")

# Enter the data retrieved into xlsx format
column_names = ["Company", "Price", "Change", "Volume"]
daf = pd.DataFrame(columns=column_names)
for i in all:
    index = 0
    daf.loc[index] = i
    daf.index = daf.index + 1
daf = daf.reset_index(drop=True)
daf.to_excel('stocks.xlsx')