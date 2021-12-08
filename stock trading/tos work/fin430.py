import requests
import json
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import math
import pprint

mutual_df = pd.read_csv('mutual.csv')
print(mutual_df)
ticker_search_list = list(trade_data_df['Symbol'])
SPY_end = datetime.datetime.now() - datetime.timedelta(2)
SPY_start = SPY_end-datetime.timedelta(368)
spy_df = web.DataReader('SPY', 'yahoo', SPY_start, SPY_end)
