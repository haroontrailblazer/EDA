import pandas as pd
import matplotlib.pyplot as pt
import numpy as np
import seaborn as sp
from statsmodels.tsa.seasonal import seasonal_decompose
#creating a date from 01-01-2021 to 30-12-2030
#the data dosen't contains any noise you easily visualize an positive linear trend in it
date=pd.date_range(start='01-01-21',end='30-12-30',freq='D')
#creating a valus column with parallel to date range
values=np.random.random_integers(1,1000,size=len(date))
df=pd.DataFrame({'date':date,'values':values})
s=seasonal_decompose(df["values"],model='additive',period=9)
e=s.resid
t=s.trend
s=s.seasonal
pt.figure(figsize=(14,10))
pt.subplot(411)
pt.plot(df['date'],df['values'],label='Original values',color='grey')
pt.legend()

pt.subplot(412)
pt.plot(df['date'],t,label='Trend',color='red')
pt.legend()

pt.subplot(413)
pt.plot(df['date'],e,label='rediual dara',color='green')
pt.legend()

pt.subplot(414)
pt.plot(df['date'],s,label='Seasonal',color='purple')
pt.legend()
pt.tight_layout()
pt.show()