import numpy as np
import matplotlib.pyplot as plt

# Define stress-strain relationship for elastic material
def stress_strain_elastic(strain, E):
    return E * strain

# Define stress-strain relationship for nonelastic material
def stress_strain_nonelastic(strain, E, yield_strain, plastic_modulus):
    stress = np.zeros_like(strain)
    for i, eps in enumerate(strain):
        if eps <= yield_strain:
            stress[i] = E * eps
        else:
            stress[i] = E * yield_strain + plastic_modulus * (eps - yield_strain)
    return stress

# Parameters
E_elastic = 200e9  # Young's modulus for elastic material (Pa)
E_nonelastic = 100e9  # Initial Young's modulus for nonelastic material (Pa)
yield_strain = 0.01  # Yield strain for nonelastic material
plastic_modulus = 10e9  # Plastic modulus for nonelastic material (Pa)

# Strain range
strain = np.linspace(0, 0.05, 500)

# Stress calculations
stress_elastic = stress_strain_elastic(strain, E_elastic)
stress_nonelastic = stress_strain_nonelastic(strain, E_nonelastic, yield_strain, plastic_modulus)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(strain, stress_elastic, label='Elastic Material', color='b')
plt.plot(strain, stress_nonelastic, label='Nonelastic Material', color='r')
plt.xlabel('Strain')
plt.ylabel('Stress (Pa)')
plt.title('Stress-Strain Curve')
plt.legend()
plt.grid(True)
plt.show()
