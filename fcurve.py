import numpy as np
import matplotlib.pyplot as plt

# define time and tau
t = np.linspace(0, 10, 100)
tau = 2

# F curve
F = 1 - np.exp(-t/tau)

plt.figure()
plt.plot(t, F)

plt.xlabel("Time (t)")
plt.ylabel("F(t)")
plt.title("Cumulative RTD (F-Curve)")
plt.grid(True)

plt.show()