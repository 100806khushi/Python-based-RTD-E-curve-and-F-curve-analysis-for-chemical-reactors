import numpy as np
import matplotlib.pyplot as plt

# Mean residence time
tau = 5   # seconds

# Time range
t = np.linspace(0, 20, 200)

# RTD E-curve equation for CSTR
E = (1/tau) * np.exp(-t/tau)

# Plotting
plt.plot(t, E)

plt.xlabel("Time (t)")
plt.ylabel("E(t)")
plt.title("Residence Time Distribution (RTD) - E-Curve")
plt.grid(True)

plt.show()