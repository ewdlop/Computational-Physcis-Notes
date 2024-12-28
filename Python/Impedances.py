import numpy as np

# Constants
R = 10  # Resistance in ohms
L = 0.01  # Inductance in henrys
C = 0.001  # Capacitance in farads
f = 50  # Frequency in Hz
omega = 2 * np.pi * f  # Angular frequency

# Impedances
Z_R = R
Z_L = 1j * omega * L
Z_C = 1 / (1j * omega * C)

# Series circuit impedance
Z_series = Z_R + Z_L + Z_C
print(f"Total impedance in series: {Z_series} ohms")

# Parallel circuit impedance
Z_parallel = 1 / (1/Z_R + 1/Z_L + 1/Z_C)
print(f"Total impedance in parallel: {Z_parallel} ohms")


# Review
# Frequency range
frequencies = np.logspace(1, 5, 400)
omega = 2 * np.pi * frequencies


# Review
# Impedance calculations
Z_R = R
Z_L = 1j * omega * L
Z_C = 1 / (1j * omega * C)

Z_series = Z_R + Z_L + Z_C
Z_parallel = 1 / (1/Z_R + 1/Z_L + 1/Z_C)

# Plotting
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(frequencies, np.abs(Z_series), label='Series Impedance')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Impedance (ohms)')
plt.title('Series Circuit Impedance')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(Z_parallel), label='Parallel Impedance')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Impedance (ohms)')
plt.title('Parallel Circuit Impedance')
plt.legend()

plt.tight_layout()
plt.show()
