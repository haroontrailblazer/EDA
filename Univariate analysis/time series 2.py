import pandas as pd
import matplotlib.pyplot as pt
import numpy as np
import seaborn as sp
from statsmodels.tsa.seasonal import seasonal_decompose
#creating a date from 01-01-2021 to 30-12-2030
#the data dosen't contains any noise you easily visualize an positive linear trend in it
date=pd.date_range(start='01-01-21',end='30-12-30',freq='D')
#creating a valus column with parallel to date range
values=np.random.randint(1,500,len(date))
df=pd.DataFrame({'date':date,'values':values})
s=seasonal_decompose(df['values'],model='additive',period=365)
t=s.trend
s=s.seasonal
pt.figure(figsize=(14,10))
pt.subplot(311)
pt.plot(df['values'],label='Original values')
pt.legend()
pt.show()

pt.subplot(312)
pt.plot(t,label='Trend')
pt.legend()
pt.show()

pt.subplot(313)
pt.plot(s,label='Seasonal')
pt.legend()
pt.show()