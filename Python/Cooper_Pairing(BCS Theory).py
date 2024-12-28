import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 100  # Number of energy states
E_F = 1.0  # Fermi energy
Delta = 0.1  # Superconducting gap

# Energy levels
E = np.linspace(-2 * E_F, 2 * E_F, N)

# BCS gap equation
def bcs_gap(E, Delta):
    return np.sqrt(E**2 + Delta**2)

# Calculate BCS gap
gap = c(E, Delta)

# Plot
plt.plot(E, gap)
plt.xlabel('Energy')
plt.ylabel('Gap')
plt.title('BCS Gap')
plt.grid(True)
plt.show()
