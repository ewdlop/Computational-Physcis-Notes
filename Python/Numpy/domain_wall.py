import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 100  # Number of spins
J = 1    # Coupling constant (ferromagnetic if J > 0)
T = 1.0  # Temperature (for future Monte Carlo simulation)

# Initialize spin configuration with a domain wall at the center
spins = np.ones(N)
spins[N//2:] = -1  # Creating a domain wall

# Function to compute energy of the system
def compute_energy(spins, J):
    energy = -J * np.sum(spins[:-1] * spins[1:])
    return energy

# Compute energy
energy = compute_energy(spins, J)

# Plot the domain wall
plt.figure(figsize=(8, 4))
plt.plot(spins, 'bo-', markersize=5, label='Spin')
plt.axvline(x=N//2, color='r', linestyle='--', label="Domain Wall")
plt.xlabel("Spin Index")
plt.ylabel("Spin Value")
plt.title(f"1D Ising Model with Domain Wall (Energy = {energy})")
plt.legend()
plt.grid()
plt.show()
