from locale import currency
import requests,json
import keys
import pandas as pd 
from time import sleep

def get_rates(base_currency='EUR', assets='BTC,ETH,XRP'):
    url=r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey=IO4FRS0W8U3DT3GR"

    payload ={'key':keys.alpha_key, 'convert':base_currency,'ids':assets, 'interval':'1d'}
    response=requests.get(url,params=payload)
    data=response.json()


    c_currency , c_price , timestamp= [] , [] , [] 

    #print(data)
    for asset in data:
        c_currency.append(['currency'])
        c_price.append(['price'])
        timestamp.append(['price_timestamp'])

    raw_data = {
        'assets':c_currency,
        'rates': c_price,
        'timestamp': timestamp

    }

    df = pd.DataFrame(raw_data)
    print(df)
    return df 


get_rates('USD','DOT')

