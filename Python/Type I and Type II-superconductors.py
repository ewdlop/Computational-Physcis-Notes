import matplotlib.pyplot as plt
import numpy as np

# Parameters
H = np.linspace(0, 2, 100)  # Magnetic field

# Type I superconductor
H_c = 1.0  # Critical field
M_type_I = np.where(H < H_c, -H, 0)

# Type II superconductor
H_c1 = 0.5  # Lower critical field
H_c2 = 1.5  # Upper critical field
M_type_II = np.where(H < H_c1, -H, np.where(H < H_c2, -H_c1, 0))

# Plot
plt.plot(H, M_type_I, label='Type I Superconductor')
plt.plot(H, M_type_II, label='Type II Superconductor')
plt.xlabel('Magnetic Field H')
plt.ylabel('Magnetization M')
plt.title('Type I and Type II Superconductors')
plt.legend()
plt.grid(True)
plt.show()
