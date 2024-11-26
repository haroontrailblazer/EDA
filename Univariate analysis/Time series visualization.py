import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random data points for temperature (between 15 and 40 degrees Celsius)
temp = np.random.randint(15, 41, 1000)

# Generate 1000 random data points for air pollution level (between 0 and 300)
airp = np.random.randint(0, 301, 1000)

# Plot Temperature data
plt.plot(temp, label='Temperature (°C)', color='orange', marker='o', markersize=4, linestyle='-')
plt.xlabel('Data Points')
plt.ylabel('Temperature (°C)', color='orange')
plt.title('Temperature Data (1000 Points)')
plt.legend(loc='upper right')
plt.grid(True)
plt.show()

# Plot Air Pollution data
plt.plot(airp, label='Air Pollution Level', color='green', marker='x', markersize=4, linestyle='-')
plt.xlabel('Data Points')
plt.ylabel('Air Pollution Level', color='green')
plt.title('Air Pollution Data (1000 Points)')
plt.legend(loc='upper right')
plt.grid(True)
plt.show()

# Print the data points for verification
print("Temperature Data Points:", temp)
print("Air Pollution Data Points:", airp)
