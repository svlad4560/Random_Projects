import requests
import pprint
from tkinter import *
import pandas as pd

url = 'https://financialmodelingprep.com/api/v3/financial-statements/BA?datatype=zip&apikey=2ead9f70179604e6f27f2a8fe3ffcf4a'
key = '2ead9f70179604e6f27f2a8fe3ffcf4a'

data = requests.get(url).json()

# print(data)
pprint.pprint(data)
