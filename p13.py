import matplotlib.pyplot as plt 
import numpy as np 
# Generate values for x-axis 
x = np.linspace(0, 2 * np.pi, 1000)  # 1000 points from 0 to 2π 
# Compute sine wave values with different frequencies 
y1 = np.sin(x)  # Sine wave with frequency 1 Hz 
y2 = np.sin(2 * x)  # Sine wave with frequency 2 Hz 
trimmed 
# Create the plot 
plt.plot(x, y1, label='Sine Wave 1 Hz')
plt.plot(x, y2, label='Sine Wave 2 Hz', linestyle='--') 
# Add labels and title 
plt.xlabel('X-axis (radians)') 
plt.ylabel('Y-axis (amplitude)') 
plt.title('Two Sine Waves') 
plt.legend() 
# Display the plot 
plt.show()
