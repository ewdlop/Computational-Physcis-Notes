import numpy as np
import matplotlib.pyplot as plt

# Parameters
m1 = 1.0  # Mass of atom 1
m2 = 2.0  # Mass of atom 2
k = np.linspace(-np.pi, np.pi, 100)  # Wave vector

# Spring constant
K = 1.0

# Dispersion relation for diatomic chain
omega_acoustic = np.sqrt(K * (1/m1 + 1/m2 - np.sqrt((1/m1 + 1/m2)**2 - 4/(m1*m2) * (np.sin(k/2)**2))))
omega_optical = np.sqrt(K * (1/m1 + 1/m2 + np.sqrt((1/m1 + 1/m2)**2 - 4/(m1*m2) * (np.sin(k/2)**2))))

# Plot
plt.plot(k, omega_acoustic, label='Acoustic Branch')
plt.plot(k, omega_optical, label='Optical Branch')
plt.xlabel('Wave vector k')
plt.ylabel('Frequency ω')
plt.title('Dispersion Relation for a Linear Diatomic Chain')
plt.grid(True)
plt.legend()
plt.show()
