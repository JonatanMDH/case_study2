# Importing some weird add-ons
import numpy as np
from matplotlib import pyplot as plt



# Defining a function to calculate the power
def calculate_power(speed):
    p = 0.85
    q = 4500

    power_pro = p * speed ** 2
    power_ind = q / speed ** 2
    power_tot = power_pro + power_ind

    return power_tot



# Deviding the two points into many multiple points
speed = np.linspace(5, 14, 100)
power_tot = calculate_power(speed)




# Plotting the data
plt.plot(speed, power_tot)
plt.plot(8.5, 123.70, marker = 'o')




#Adding labels, title and grid
plt.xlabel("Flight speed (m/s)")
plt.ylabel("Power (W/kg)")
plt.title("Some weird flying bird")


