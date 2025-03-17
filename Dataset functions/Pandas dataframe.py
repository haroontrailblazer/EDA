import pandas as pd
df=pd.DataFrame({'reg.no':[621823243011,621823243012,621823243013,621823243014,621823243015,621823243016,621823243017,621823243018,621823243019,621823243020],
              'Name':['Arun','Bala','Chandru','Dinesh','Eswar','Fayaz','Ganesh','Hari','Irfan','Jagan'],'Rank':['a+','a','b+','b','c+','c','d+','d','e+','e']}).set_index('reg.no')
print(df)
print(df.loc[621823243011])
print(df[df['Name']=='Arun'])
print(df[df['Rank']=='a+'])