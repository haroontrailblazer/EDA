
import pandas as pd
import matplotlib.pyplot as mp
import matplotlib.dates as mdates
from statsmodels.tsa.holtwinters import ExponentialSmoothing
print("\n• If the frequency is Minutewise Enter(N)\n• If the frequency is Hourly Enter(H)\n• If the frequency is Daywise Enter(D)\n• If the frequency is weekely Enter(W)\n• If the frequency is Monthly Enter(M)\n• If the frequency is yearly Enter(Y)\n")
n1=input("\n\nEnter your Date and Time frequency: ");n2=int(input("Enter your no.of.forcasing steps: "));fp=input(r"\nEnter the previous data file:")
df=pd.read_csv(fp,parse_dates=['date']).set_index('date');df.isnull().sum();df.ffill()
if n1=='N':
    x=int(input('how many hours data you have: '))
    df_min=df.resample('min').mean().ffill()
    model=ExponentialSmoothing(df_min['close'],trend='additive',seasonal='add',seasonal_periods=x);dd=model.fit();print(dd.summary());fc=dd.forecast(n2)
    mp.plot(df_min['close'],color='blue',label='Trend');mp.plot(fc,color='red',label='Prediction');mp.legend();mp.title('Stock Analysis');ax = mp.gca();ax.xaxis.set_major_formatter(mdates.DateFormatter('%D-%min'));mp.gcf().autofmt_xdate();mp.show()
elif n1=='H':
    x=int(input('how many days data you have: '))
    df_hourly=df.resample('h').mean().ffill()
    model=ExponentialSmoothing(df_hourly['close'],trend='additive',seasonal='add',seasonal_periods=x);dd=model.fit();print(dd.summary());fc=dd.forecast(n2)
    mp.plot(df_hourly['close'],color='blue',label='Trend');mp.plot(fc,color='red',label='Prediction');mp.legend();mp.title('Stock Analysis');ax = mp.gca();ax.xaxis.set_major_formatter(mdates.DateFormatter('%D-%h'));mp.gcf().autofmt_xdate();mp.show()
elif n1=='D':
    x=int(input('how many months data you have: '))
    df_daily=df.resample('d').mean().ffill()
    model=ExponentialSmoothing(df_daily['close'],trend='additive',seasonal='add',seasonal_periods=x);dd=model.fit();print(dd.summary());fc=dd.forecast(n2)
    mp.plot(df_daily['close'],color='blue',label='Trend');mp.plot(fc,color='red',label='Prediction');mp.legend();mp.title('Stock Analysis');ax = mp.gca();ax.xaxis.set_major_formatter(mdates.DateFormatter('%D'));mp.gcf().autofmt_xdate();mp.show()
elif n1=='W':
    x=int(input('how many months you have: '))
    df_weekely=df.resample('W').mean().ffill()
    model=ExponentialSmoothing(df_weekely['close'],trend='additive',seasonal='add',seasonal_periods=x);dd=model.fit();print(dd.summary());fc=dd.forecast(n2)
    mp.plot(df_weekely['close'],color='blue',label='Trend');mp.plot(fc,color='red',label='Prediction');mp.legend();mp.title('Stock Analysis');ax = mp.gca();ax.xaxis.set_major_formatter(mdates.DateFormatter('%D'));mp.gcf().autofmt_xdate();mp.show()
elif n1=='M':
    x=int(input('how many years data you have: '))
    df_monthly=df.resample('ME').mean().ffill()
    model=ExponentialSmoothing(df_monthly['close'],trend='additive',seasonal='add',seasonal_periods=x);dd=model.fit();print(dd.summary());fc=dd.forecast(n2)
    mp.plot(df_monthly['close'],color='blue',label='Trend');mp.plot(fc,color='red',label='Prediction');mp.legend();mp.title('Stock Analysis');ax = mp.gca();ax.xaxis.set_major_formatter(mdates.DateFormatter('%D'));mp.gcf().autofmt_xdate();mp.show()