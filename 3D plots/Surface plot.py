import numpy as np
import matplotlib.pyplot as mp
x=np.linspace(-10,10,100)
y=np.linspace(-10,10,100)
x1,y1=np.meshgrid(x,y)
z=x1**2+y1**2
a=mp.subplot(projection='3d')
a.plot_surface(x1,y1,z,color='b')
mp.show()