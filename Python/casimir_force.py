import numpy as np

# Parameters
h = 6.626e-34  # Planck's constant in Js
c = 3e8  # Speed of light in m/s
a = 1e-9  # Separation between plates in meters

# Casimir force per unit area
def casimir_force(a):
    return -np.pi**2 * h * c / (240 * a**4)

# Calculate force
force = casimir_force(a)
print("Casimir force per unit area:", force, "N/m^2")
