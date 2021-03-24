import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import itertools
import requests
import json

test_list = [1,2,3,4,5,6,7,8,9,10]
test_pd = pd.DataFrame()
test_pd['1'] = test_list

test_pd.to_csv('testing123.csv')
