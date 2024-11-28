import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
import seaborn as sp
from scipy import stats
cols=[]
fp=str(input(r"Enter the file path: "))
df=pd.read_csv(fp,low_memory=False);print("\nOiginal data:\n",df);print("\nThe null data rows are\n",df.isnull().sum())
dfc=df.dropna();print("\ncleaned data:\n",dfc)
gn=input("Enter the fields name:").split(",");n=len(gn)
for i in range(1,n+1):
    cl=gn[i-1];cols.append(cl);da=dfc[cl].values.reshape(-1,1);print(i,":\n",da)
    print("\n SUMMARY STATISTICAL ANALYSIS OF: ",cl,"\n FIVE NUMBER SUMMARY: ")
    print("\n Minimum value:",min(da),"\n 25th quantile value:",np.quantile(da,0.25),"\n 50th quantile value:",np.quantile(da,0.5),"\n 75th quantile value:",np.quantile(da,0.75),"\n Maximum value:",np.max(da))
    print("\n MEASURE OF CENTRAL TENDENCY:","\n Mean= ",np.mean(da),"\n Median= ",np.median(da),"\n Mode= ",stats.mode(da))
    print("\n MEASURE OF DISPERSION:","\n Range= ",np.var(da),"\n Variance= ",np.ptp(da),"\n Standard deviation= ",np.std(da))
    print("\nMeasure of Shape:","\nSkewness:",stats.skew(da),"\nKurtosis:",stats.kurtosis(da))
    mp.hist(da,bins=25,label='No.of.propotions',color='purple');mp.xlabel(cols[i-1]);mp.legend();mp.show()
    sc=dfc[cl].value_counts().sort_index();sc.plot(kind='bar',label='No.of.propotions');mp.xlabel(cols[i-1]);mp.legend();mp.show()
    sp.boxplot(da,label='No.of.propotions');mp.xlabel(cols[i-1]);mp.legend();mp.show()
    sk=dfc[cl].value_counts().sort_values();sk.plot(kind='pie',autopct='%1.1f%%',label='No.of.propotions');mp.legend();mp.title(cols[i-1]);mp.show()
    sp.kdeplot(da,fill=True);mp.xlabel(cols[i-1]);mp.show()
print(cols)
if n==2:
    x1=df[cols[0]];y=df[cols[1]];mp.scatter(x1,y);mp.xlabel(cols[0]);mp.ylabel(cols[1]);mp.title('Analysis of Factor');mp.show()
    mp.plot(x1,y);mp.xlabel(cols[0]);mp.ylabel(cols[1]);mp.title('Analysis of Factors');mp.show()
    mp.hexbin(x1,y,gridsize=25);mp.colorbar();mp.xlabel(cols[0]);mp.ylabel(cols[1]);mp.title('Analysis of Factor');mp.show()
    mp.bar(x1,y);mp.xlabel(cols[0]);mp.ylabel(cols[1]);mp.title('Analysis of Factor');mp.show()
    sp.regplot(x=x1,y=y);mp.xlabel(cols[0]);mp.ylabel(cols[1]);mp.title('Analysis of Factor');mp.show()
    sp.violinplot(x1,label=cols[0]);sp.violinplot(y,label=cols[1]);mp.xlabel(cols[0]);mp.legend();mp.title('Analysis of factors');mp.show()
    mp.pie([np.sum(x1),np.sum(y)],autopct='%1.1f%%',labels=[cols[0],cols[1]]);mp.legend();mp.title('Analysis of factors');mp.show()
elif n==3:
    x1=df[cols[0]];y=df[cols[1]];z=df[cols[2]];mp.scatter(x1,y,label=cols[1]);mp.scatter(x1,z,label=cols[2]);mp.xlabel(cols[0]);mp.ylabel('Factors');mp.title('Analysis of Factors');mp.legend();mp.show()
    mp.plot(x1,y,label=cols[1]);mp.plot(x1,z,label=cols[2]);mp.xlabel(cols[0]);mp.ylabel('Factors');mp.title('Analysis of Factors');mp.legend();mp.show()
    mp.hexbin(x1,y,gridsize=25,label=cols[1],color='red');mp.hexbin(x1,z,gridsize=25,label=cols[2],color='blue');mp.colorbar();mp.xlabel(cols[0]);mp.ylabel('Factors');mp.title('Analysis of Factors');mp.legend();mp.show()
    mp.bar(x1,y,label=cols[1],color='red');mp.bar(x1,z,label=cols[2],color='blue');mp.xlabel(cols[0]);mp.ylabel('Factors');mp.title('Analysis of Factors');mp.legend();mp.show()
    sp.regplot(x=x1,y=y,label=cols[1]);sp.regplot(x=x1,y=z,label=cols[2]);mp.xlabel(cols[0]);mp.ylabel('Factors');mp.title('Analysis of Factors');mp.legend();mp.show()
    sp.violinplot(x1,label=cols[0]);sp.violinplot(y,label=cols[1]);sp.violinplot(z,label=cols[2]);mp.xlabel(cols[0]);mp.legend();mp.title('Analysis of factors');mp.show()
    mp.pie([np.sum(x1),np.sum(y),np.sum(z)],autopct='%1.1f%%',labels=[cols[0],cols[1],cols[2]]);mp.legend();mp.title('Analysis of factors');mp.show()
else:
    print("\n")
