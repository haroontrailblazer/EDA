import numpy as np
import matplotlib.pyplot as mp
x=np.linspace(-10,10,100)
y=np.linspace(-10,10,100)
x1,y1=np.meshgrid(x,y)
z=x1**2+y1**2
cl=mp.colormaps()
for i in range(0,len(cl)):
    print(i+1 ,cl[i])
    a=mp.subplot(projection='3d')
    a.plot_surface(x1,y1,z,cmap=cl[i])
    mp.show()
