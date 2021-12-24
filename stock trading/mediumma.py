from backtesting import Strategy
from backtesting.lib import crossover
# Function to return the SMA
def SMA(values, n):
    return pd.Series(values).rolling(n).mean()
class SmaCross(Strategy):
    # Define the two MA lags as *class variables*
    ma_short = 10
    ma_long = 20
    df = df

    def init(self):
        # Precompute the two moving averages
        self.sma1 = self.I(SMA, self.df.Close.to_numpy(), self.ma_short)
        self.sma2 = self.I(SMA, self.df.Close.to_numpy(), self.ma_long)

    def next(self):
        # If sma1 crosses above sma2 buy the asset
        if crossover(self.sma1, self.sma2):
            self.buy()
# Else, if sma1 crosses below sma2 sell the asset
        elif crossover(self.sma2, self.sma1):
            self.position.close()


# group
hm = heatmap.groupby(['ma_short', 'ma_long']).mean().unstack()
#plot heatmap
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(12, 10))
sns.heatmap(hm[::-1], cmap='viridis')
