import requests
import pprint
from tkinter import *
import pandas as pd

searched_stock = "AMZN"
list_of_stocks = ['BNED','DBX','GOOG','KOPN','MGM','QS','RXT','STKL','TSLA','TWLO','WMT']
url ="https://financialmodelingprep.com/api/v3/profile/"+searched_stock+"?apikey=2ead9f70179604e6f27f2a8fe3ffcf4a"
data = requests.get(url).json()
data_pd = pd.DataFrame(data)

last_price = int(data_pd["price"])
dcf = int(data_pd["dcf"])
beta_list = []
for i in list_of_stocks:
    stock = i
    url ="https://financialmodelingprep.com/api/v3/profile/"+stock+"?apikey=2ead9f70179604e6f27f2a8fe3ffcf4a"
    data = requests.get(url).json()
    data_pd = pd.DataFrame(data)
    beta = float(data_pd['beta'])
    beta_list.append(beta)
beta_pd = pd.DataFrame(beta_list)
beta_pd.to_csv('beta.csv')
# print(beta_list)
