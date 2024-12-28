import numpy as np
import matplotlib.pyplot as plt

# Define the potential function
def potential(z):
    return np.real(z)  # Example: potential is the real part of the complex number

# Define the conformal map
def conformal_map(z):
    return np.log(z)  # Example: logarithmic map

# Define the inverse conformal map
def inverse_conformal_map(w):
    return np.exp(w)  # Example: inverse of the logarithmic map

# Define the computational grid
x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Apply the conformal map
W = conformal_map(Z)

# Solve the potential in the transformed domain
Phi = potential(W)

# Map the solution back to the original domain
Phi_original = np.real(inverse_conformal_map(W))

# Plot the results
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.contourf(X, Y, Phi, 50, cmap='jet')
plt.colorbar()
plt.title("Potential in Transformed Domain")

plt.subplot(1, 2, 2)
plt.contourf(X, Y, Phi_original, 50, cmap='jet')
plt.colorbar()
plt.title("Potential in Original Domain")

plt.tight_layout()
plt.show()
