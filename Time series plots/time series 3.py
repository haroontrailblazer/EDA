import pandas as pd
import matplotlib.pyplot as pt
import numpy as np
from statsmodels.tsa.stattools import adfuller
#creating a date from 01-01-2021 to 30-12-2030
#the data dosen't contains any noise you easily visualize an positive linear trend in it
date=pd.date_range(start='01-01-21',end='30-12-30',freq='M')
#creating a valus column with parallel to date range
values=np.random.random_integers(1,100,size=len(date))
df=pd.DataFrame({'date':date,'values':values})
#finding hypothesis
r=adfuller(df['values'],autolag="AIC")
if r[1]<=0.05:
    print("Rject null hypothesis.The time series is likely stationary")
else:
    print("The time series may contains a 'Trend'")
df['dvalues']=df['values'].diff()
print(df)
pt.plot(df['date'],df['values'],label='Original values',color="red")
pt.plot(df['date'],df['dvalues'],label='Differenciated values',color="purple")
pt.legend()
pt.show()