import pandas as pd
import matplotlib.pyplot as mp
import matplotlib.dates as mdates
from statsmodels.tsa.holtwinters import ExponentialSmoothing
fp=input(r"\nEnter the previous data file:")
df=pd.read_csv(fp,parse_dates=['date']).set_index('date')
df.isnull().sum();df.ffill()
df_daily=df.resample('D').mean().ffill()
model=ExponentialSmoothing(df_daily['close'],trend='additive',seasonal='add',seasonal_periods=117)
dd=model.fit()
print(dd.summary())
fc=dd.forecast(1514)
mp.plot(df_daily['close'],color='blue',label='Trend')
mp.plot(fc,color='red',label='Prediction')
mp.legend()
mp.title('WIPRO Stock Analysis')
ax = mp.gca()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%D'))
mp.gcf().autofmt_xdate()
mp.show()
