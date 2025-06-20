import pandas as pd
import matplotlib.pyplot as pt
import numpy as np
import seaborn as sp

#creating a date from 01-01-2021 to 30-12-2030
#the data dosen't contains any noise you easily visualize an positive linear trend in it
date=pd.date_range(start='01-01-21',end='30-12-30',freq='M')

#creating a valus column with parallel to date range
values=np.linspace(1,750,len(date))
ip=values+np.random.random_integers(1,40,len(date))
df=pd.DataFrame({'date':date,'values':ip})

#creating seperate column for year,day,month
df['year']=df['date'].dt.year
df['day']=df['date'].dt.day
df['month']=df['date'].dt.month
print(df)
df.info()

pt.style.use('dark_background')
pt.plot(df['date'],df['values'],linestyle='-',marker='o',color='red',label='trends')
pt.title('time series analysis')
pt.xlabel('date')
pt.ylabel('values')
pt.legend()
pt.show()

sp.lineplot(x=df['date'],y=df['values'],label='trends')
pt.title('time series analysis')
pt.xlabel('date')
pt.ylabel('values')
pt.legend()
pt.show()