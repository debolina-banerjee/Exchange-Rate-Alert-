import os
import smtplib
import imghdr
from email.message import EmailMessage

import yfinance as yf
import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr

# your email and your password
# to send Alert mail to other email accounts
EMAIL_ADDRESS="debolina.banerjee2019@gmail.com"
EMAIL_PASSWORD='xytvpzygiqywavyf'

msg=EmailMessage()

yf.pdr_override()
start=dt.datetime(2022,9,9)
now =dt.datetime.now()

stock="BTC-USD"
TargetPrice=330

msg["Subject"]="Alert on"+stock
msg["From"]=EMAIL_ADDRESS
msg["To"]="debolina.ad2024@gmail.com"

alerted=False

while 1:
    df=pdr.get_data_yahoo(stock, start, now)
    currentClose=df["Adj Close"][-1]
    print(currentClose)

    condition=currentClose>TargetPrice

    if(condition and alerted==False):
        alerted=True
        message= stock +"Has activated the alert price of "+ str(TargetPrice) +\
            "\nCurrent Price: "+str(currentClose)
        
        msg.set_content(message)
        
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            smtp.send_message(msg)

            print("Completed")
    else:
        print(" no new Alerts")
        
    #time.sleep(60) 