import numpy as np
import matplotlib.pyplot as plt

# Parameters
a = 1.0  # Lattice constant
N = 100  # Number of atoms
k = np.linspace(-np.pi/a, np.pi/a, N)

# Phonon dispersion relation
def phonon_dispersion(k, a):
    return np.sqrt(2 * (1 - np.cos(k * a)))

# Calculate dispersion
omega = phonon_dispersion(k, a)

# Plot
plt.plot(k, omega)
plt.xlabel('Wave vector k')
plt.ylabel('Frequency ω')
plt.title('Phonon Dispersion Relation')
plt.grid(True)
plt.show()
