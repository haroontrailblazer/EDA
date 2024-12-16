import matplotlib.pyplot as mp
import seaborn as sp
#createc a random number set fot the variable data
data=[18, 20, 22, 21, 24, 30, 28, 27, 33, 35, 38, 40, 42, 45]
sp.kdeplot(data,fill=True)
mp.show()