import numpy as np
import matplotlib.pyplot as plt

# Mean residence time
tau = 5  

# Time range
t = np.linspace(0, 20, 400)

# RTD for CSTR
E_cstr = (1/tau) * np.exp(-t/tau)

# Cumulative distribution
F_cstr = 1 - np.exp(-t/tau)

# Approximate RTD for PFR (narrow Gaussian peak around tau)
sigma = 0.3
E_pfr = (1/(sigma*np.sqrt(2*np.pi))) * np.exp(-(t-tau)**2/(2*sigma**2))

# Plot
plt.figure(figsize=(8,5))

plt.plot(t, E_cstr, color='blue', linewidth=2, label='E(t) - CSTR')
plt.plot(t, F_cstr, color='green', linewidth=2, linestyle='--', label='F(t) - CSTR')
plt.plot(t, E_pfr, color='red', linewidth=2, label='E(t) - PFR')

plt.xlabel("Time (t)")
plt.ylabel("Distribution Function")
plt.title("Residence Time Distribution (RTD) Comparison")
plt.legend()
plt.grid(True)

plt.show()