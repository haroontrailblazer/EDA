import pandas as pd
import numpy as np

#creating a date from 01-01-2021 to 30-12-2030
#the data dosen't contains any noise you easily visualize an positive linear trend in it
date=pd.date_range(start='01-01-21',end='30-12-30',freq='H')

#creating a valus column with parallel to date range
values=np.linspace(1,1000,len(date))

#creating noise over the data
ip=values+np.random.random_integers(1,100,len(date))
df=pd.DataFrame({'date':date,'values':ip})
df.set_index('date',inplace=True)
print(df)

#resampling of date for conviniance
daily=df.resample("D").mean()
print(f'Daily Resampling\n{daily}')

monthly=df.resample("M").mean()
print(f'Monthly Resampling\n{monthly}')

s30min=df.resample("30T").ffill()
print(f'30 Mins Resampling\n{s30min}')

weekely=df.resample("W").sum()
print(f'Weekley resampling:\n{weekely}')

#date and time aggregation
dfcombo=df.resample("30MIN").ffill().resample("D").mean()
print(f'Date & Time Aggregation\n{dfcombo}')