import matplotlib.pyplot as mp
mp.style.available
# List of available styles
for i in range(0,len(mp.style.available)):
    # Set the style
    mp.style.use(mp.style.available[i])

    # using a simple sine wave as an example
    import numpy as np
    # Generate values for x-axis 
    x = np.linspace(0, 2 * np.pi, 1000)  # 1000 points from 0 to 2π 
    # Compute sine wave values with different frequencies 
    y1 = np.sin(x)  # Sine wave with frequency 1 Hz 
    y2 = np.sin(2 * x)  # Sine wave with frequency 2 Hz trimmed 
    # Create the plot
    mp.plot(x, y1, label='Sine Wave 1 Hz')
    mp.plot(x, y2, label='Sine Wave 2 Hz', linestyle='--') 
    # Add labels and title 
    mp.xlabel('X-axis (radians)') 
    mp.ylabel('Y-axis (amplitude)') 
    mp.title('Two Sine Waves') 
    s=i+1,mp.style.available[i]
    mp.text(0.494,-0.850,s) 
    mp.legend() 
    print(i+1 ,mp.style.available[i])
    # Display the plot 
    mp.show()