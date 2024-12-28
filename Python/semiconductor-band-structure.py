import numpy as np
import matplotlib.pyplot as plt

# Parameters
a = 1.0  # Lattice constant
E_g = 1.0  # Band gap energy
t_c = 0.5  # Effective mass term for conduction band
t_v = 0.5  # Effective mass term for valence band

# Wave vectors
k = np.linspace(-np.pi/a, np.pi/a, 200)

# Conduction band (parabolic approximation)
E_c = E_g / 2 + t_c * (k * a)**2

# Valence band (parabolic approximation)
E_v = -E_g / 2 - t_v * (k * a)**2

# Plot
plt.plot(k, E_c, label='Conduction Band')
plt.plot(k, E_v, label='Valence Band')
plt.axhline(y=0, color='k', linestyle='--', linewidth=0.8, label='Fermi Level (E_F)')
plt.xlabel('Wave vector k')
plt.ylabel('Energy E')
plt.title('Simplified Band Structure of a Semiconductor')
plt.grid(True)
plt.legend()
plt.show()
