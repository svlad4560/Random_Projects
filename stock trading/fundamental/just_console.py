import requests
import pprint
from tkinter import *
import pandas as pd

searched_stock = "AMZN"

url ="https://financialmodelingprep.com/api/v3/profile/"+searched_stock+"?apikey=2ead9f70179604e6f27f2a8fe3ffcf4a"
data = requests.get(url).json()
data_pd = pd.DataFrame(data)

last_price = int(data_pd["price"])
dcf = int(data_pd["dcf"])

if last_price > dcf :
    print("last is greater than dcf")
else:
    print("last price ")
