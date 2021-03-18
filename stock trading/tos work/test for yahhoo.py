import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


end = dt.datetime.now()
start = end-dt.timedelta(5)

morning_time = dt.time(4,00,00)

df = web.DataReader("TSLA", 'yahoo', start, end)
# if end > dt.time(12,30,00):
#     print('it is now past 12')
# print(dt.datetime.now().strftime('%M:%S.%f')[:-4])
# print(end.time())
# print(morning_time)
print(df)

restriction = end.time()

if morning_time > restriction:
    print('not restricted')

else:
    print('restricted')
