import pandas as pd
import numpy as np
from scipy import stats
from sklearn.preprocessing import scale
from sklearn.preprocessing import minmax_scale


print("\n                        SUMMARY STATISTICAL ANALYSIS")

fp = (input("\nEnter your file path :"))
df = pd.read_csv(fp,low_memory=False)
print(dfc=df.dropna());dfc.info()
col = str(input("Enter your field name :")) 
ip = dfc[[col]].values.reshape(-1,1)


print("\n                 Normal dataset :",ip)



m = np.mean(ip)
me = np.median(ip)
mo = stats.mode(ip)
sd = np.std(ip)
var = np.var(ip)
ra = np.ptp(ip)
sk = stats.skew(ip)
ku = stats.kurtosis(ip)
qua = np.quantile(ip,0.25)
qu = np.quantile(ip,0.50)
c =np.quantile(ip,0.75)
sca = minmax_scale(ip)
stand = scale(ip)
nor = ((ip-np.min(ip))/(np.max(ip)+np.min(ip)))

print("\nMean value =",m)
print("Median value =",me)
print("Mode value =",mo)
print("Standard deviation =",sd)
print("Variance =",var)
print("Range =",ra)
print("Skewness value =",sk)
print("Kurtosis value =",ku)
print("Quantile of 25th =",qua)
print("Quantile of 50th =",qu)
print("Quantile of 75th =",c)
print("\n                 Scaled data values :",sca)
print("\n                 Standardized data values :",stand)
print("\n                 Normalized data values",nor)
