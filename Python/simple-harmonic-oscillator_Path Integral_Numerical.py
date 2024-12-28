import numpy as np
import matplotlib.pyplot as plt

# Constants
m = 1.0       # mass
omega = 1.0   # angular frequency
hbar = 1.0    # reduced Planck's constant
N = 100       # number of time slices
T = 1.0       # total time
dt = T / N    # time step
x_i = 0.0     # initial position
x_f = 1.0     # final position

# Generate paths
def generate_paths(x_i, x_f, N):
    paths = []
    for _ in range(100):  # number of paths
        x = np.zeros(N + 1)
        x[0], x[-1] = x_i, x_f
        for i in range(1, N):
            x[i] = np.random.normal(0, np.sqrt(hbar * dt / m))
        paths.append(x)
    return paths

# Compute the action for a given path
def action(path):
    S = 0.0
    for i in range(N):
        x = path[i]
        x_next = path[i + 1]
        S += 0.5 * m * ((x_next - x) / dt)**2 * dt - 0.5 * m * omega**2 * x**2 * dt
    return S

# Compute the propagator
def propagator(paths):
    K = 0.0
    for path in paths:
        S = action(path)
        K += np.exp(1j * S / hbar)
    return K / len(paths)

# Generate paths and compute the propagator
paths = generate_paths(x_i, x_f, N)
K = propagator(paths)

# Print the result
print(f"Propagator K(x_f={x_f}, t_f={T}; x_i={x_i}, t_i=0): {K}")

# Plot some paths
plt.figure(figsize=(10, 6))
for path in paths[:10]:  # plot 10 paths
    plt.plot(np.linspace(0, T, N + 1), path)
plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Sample Paths for the Simple Harmonic Oscillator')
plt.grid(True)
plt.show()
