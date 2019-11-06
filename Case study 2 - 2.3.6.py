# Importing some weird add-ons
import numpy as np
from matplotlib import pyplot as plt


# Mass is not defined, so we need to make up multiple masses
mass = np.linspace(0, 12, 100)    

# Formula to calculate the required power
power_req = mass**(7/6)
power_av = mass**(2/3)


# Plotting the graph and adding labels
plt.plot(mass, power_req, label="Required power")
plt.plot(mass, power_av, label="Available power")
plt.xlabel("Mass (kg)")
plt.ylabel("Required power (Watt)")
plt.title("Some weird flying bird")
plt.grid()
plt.legend()









