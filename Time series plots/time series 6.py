import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import matplotlib.pyplot as mp
date=pd.date_range(start='01-01-2023',end='30-12-2023',freq='D')
values=np.linspace(1,750,len(date))
ip=values+np.random.random_integers(1,30,len(date))
f1=values+np.random.random_integers(1,30,len(date))
df=pd.DataFrame({'date':date,'values':ip,'featue1':f1})
dfc=df[["date","values"]].set_index("date")
print(dfc)
model=SimpleExpSmoothing(dfc['values'])
r=model.fit()
print(r.summary())
dmodel=ExponentialSmoothing(dfc['values'],trend='additive')
s=dmodel.fit()
print(s.summary())
tmodel=ExponentialSmoothing(dfc['values'],trend='additive',seasonal='add',seasonal_periods=3)
t=tmodel.fit()
print(t.summary())
s=30
y=t.forecast(steps=s)
print(dfc)
print(y)
d = pd.date_range(start='2024-01-01', periods=s)
mp.figure(figsize=(12, 6)) 
mp.plot(dfc['values'], label='Fitted Data') 
mp.plot(d, y, label='Forecast') 
mp.title('Exponential Smoothing Forecast')
mp.xlabel('Date') 
mp.ylabel('Values') 
mp.legend() 
mp.show()