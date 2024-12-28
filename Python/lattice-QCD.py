import numpy as np

# Parameters
L = 4  # Lattice size
beta = 2.5  # Inverse coupling constant

# Initialize lattice with random phases
lattice = np.exp(1j * np.random.uniform(0, 2 * np.pi, (L, L, L, L)))

# Function to calculate the plaquette
def plaquette(lattice, beta):
    plaq = 0.0
    for mu in range(4):
        for nu in range(mu + 1, 4):
            plaq += np.mean(np.real(np.trace(np.dot(lattice, np.roll(lattice, shift=-1, axis=mu)))))
    return plaq * beta

# Calculate plaquette
plaq = plaquette(lattice, beta)
print("Plaquette value:", plaq)
