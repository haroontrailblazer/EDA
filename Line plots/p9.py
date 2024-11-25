import matplotlib.pyplot as dv 
import numpy as np 
t1=np.arange(0,100,10) 
t2=np.arange(0,100,5) 
t3=np.arange(0,100,2) 
dv.plot(t1,'r--', t2, 'bs', t3, 'g^') 
print(t1, t2, t3) 
dv.xlabel('Plot with red dashes - blue squares and green triangles') 
dv.show()
