import pandas as pd
import matplotlib.pyplot as pt
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
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
lags=[20,40,50]
for i in lags:
    plot_acf(df['values'],lags=i,label=i)
    pt.legend()
    pt.title('autocoorelation plot')
    pt.show()
for i in lags:
    plot_pacf(df['values'],lags=i,label=i)
    pt.legend()
    pt.title('autocoorelation plot')
    pt.show()    
