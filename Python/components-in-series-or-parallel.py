def series_capacitance(capacitors):
    return 1 / sum(1 / c for c in capacitors)

def parallel_capacitance(capacitors):
    return sum(capacitors)

def series_resistance(resistors):
    return sum(resistors)

def parallel_resistance(resistors):
    return 1 / sum(1 / r for r in resistors)

def series_inductance(inductors):
    return sum(inductors)

def parallel_inductance(inductors):
    return 1 / sum(1 / l for l in inductors)

def series_spring_constant(springs):
    return 1 / sum(1 / k for k in springs)

def parallel_spring_constant(springs):
    return sum(springs)

# Example usage
capacitors = [1e-6, 2e-6, 3e-6]  # in farads
resistors = [100, 200, 300]  # in ohms
inductors = [1e-3, 2e-3, 3e-3]  # in henrys
springs = [100, 200, 300]  # in N/m

print("Series Capacitance:", series_capacitance(capacitors), "F")
print("Parallel Capacitance:", parallel_capacitance(capacitors), "F")
print("Series Resistance:", series_resistance(resistors), "Ohms")
print("Parallel Resistance:", parallel_resistance(resistors), "Ohms")
print("Series Inductance:", series_inductance(inductors), "H")
print("Parallel Inductance:", parallel_inductance(inductors), "H")
print("Series Spring Constant:", series_spring_constant(springs), "N/m")
print("Parallel Spring Constant:", parallel_spring_constant(springs), "N/m")


import subprocess
import sys

def install_package(package):
    """
    Install the given package using pip and capture the output.
    
    Parameters:
    package (str): The name of the package to install.
    
    Returns:
    str: The output of the pip install command.
    """
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", package],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"Successfully installed {package}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package}. Error: {e}")
        return e.stdout + e.stderr


# Define symbols for individual capacitances
C1, C2, C3 = sp.symbols('C1 C2 C3')

# Series combination using the formula
C_series = 1 / (1/C1 + 1/C2 + 1/C3)
C_series_simplified = sp.simplify(C_series)

# Parallel combination using the formula
C_parallel = C1 + C2 + C3

print(f"Series Combination of Capacitors: {C_series_simplified}")
print(f"Parallel Combination of Capacitors: {C_parallel}")

# Define symbols for individual resistances
R1, R2, R3 = sp.symbols('R1 R2 R3')

# Series combination using the formula
R_series = R1 + R2 + R3

# Parallel combination using the formula
R_parallel = 1 / (1/R1 + 1/R2 + 1/R3)
R_parallel_simplified = sp.simplify(R_parallel)

print(f"Series Combination of Resistors: {R_series}")
print(f"Parallel Combination of Resistors: {R_parallel_simplified}")

# Define symbols for individual inductances
L1, L2, L3 = sp.symbols('L1 L2 L3')

# Series combination using the formula
L_series = L1 + L2 + L3

# Parallel combination using the formula
L_parallel = 1 / (1/L1 + 1/L2 + 1/L3)
L_parallel_simplified = sp.simplify(L_parallel)

print(f"Series Combination of Inductors: {L_series}")
print(f"Parallel Combination of Inductors: {L_parallel_simplified}")

# Define symbols for individual spring constants
k1, k2, k3 = sp.symbols('k1 k2 k3')

# Series combination using the formula
k_series = 1 / (1/k1 + 1/k2 + 1/k3)
k_series_simplified = sp.simplify(k_series)

# Parallel combination using the formula
k_parallel = k1 + k2 + k3

print(f"Series Combination of Springs: {k_series_simplified}")
print(f"Parallel Combination of Springs: {k_parallel}")

# View

import sympy as sp

# Define symbols for individual capacitances
C1, C2, C3 = sp.symbols('C1 C2 C3')

# Series combination using the formula
C_series = 1 / (1/C1 + 1/C2 + 1/C3)
C_series_simplified = sp.simplify(C_series)

# Parallel combination using the formula
C_parallel = C1 + C2 + C3

# Substitute numerical values
C1_value, C2_value, C3_value = 1e-6, 2e-6, 3e-6  # in farads
C_series_value = C_series_simplified.subs({C1: C1_value, C2: C2_value, C3: C3_value})
C_parallel_value = C_parallel.subs({C1: C1_value, C2: C2_value, C3: C3_value})

print(f"Series Combination of Capacitors: {C_series_simplified} -> {C_series_value} F")
print(f"Parallel Combination of Capacitors: {C_parallel} -> {C_parallel_value} F")

# Define symbols for individual resistances
R1, R2, R3 = sp.symbols('R1 R2 R3')

# Series combination using the formula
R_series = R1 + R2 + R3

# Parallel combination using the formula
R_parallel = 1 / (1/R1 + 1/R2 + 1/R3)
R_parallel_simplified = sp.simplify(R_parallel)

# Substitute numerical values
R1_value, R2_value, R3_value = 100, 200, 300  # in ohms
R_series_value = R_series.subs({R1: R1_value, R2: R2_value, R3: R3_value})
R_parallel_value = R_parallel_simplified.subs({R1: R1_value, R2: R2_value, R3: R3_value})

print(f"Series Combination of Resistors: {R_series} -> {R_series_value} Ohms")
print(f"Parallel Combination of Resistors: {R_parallel_simplified} -> {R_parallel_value} Ohms")

# Define symbols for individual inductances
L1, L2, L3 = sp.symbols('L1 L2 L3')

# Series combination using the formula
L_series = L1 + L2 + L3

# Parallel combination using the formula
L_parallel = 1 / (1/L1 + 1/L2 + 1/L3)
L_parallel_simplified = sp.simplify(L_parallel)

# Substitute numerical values
L1_value, L2_value, L3_value = 1e-3, 2e-3, 3e-3  # in henrys
L_series_value = L_series.subs({L1: L1_value, L2: L2_value, L3: L3_value})
L_parallel_value = L_parallel_simplified.subs({L1: L1_value, L2: L2_value, L3: L3_value})

print(f"Series Combination of Inductors: {L_series} -> {L_series_value} H")
print(f"Parallel Combination of Inductors: {L_parallel_simplified} -> {L_parallel_value} H")

# Define symbols for individual spring constants
k1, k2, k3 = sp.symbols('k1 k2 k3')

# Series combination using the formula
k_series = 1 / (1/k1 + 1/k2 + 1/k3)
k_series_simplified = sp.simplify(k_series)

# Parallel combination using the formula
k_parallel = k1 + k2 + k3

# Substitute numerical values
k1_value, k2_value, k3_value = 100, 200, 300  # in N/m
k_series_value = k_series_simplified.subs({k1: k1_value, k2: k2_value, k3: k3_value})
k_parallel_value = k_parallel.subs({k1: k1_value, k2: k2_value, k3: k3_value})

print(f"Series Combination of Springs: {k_series_simplified} -> {k_series_value} N/m")
print(f"Parallel Combination of Springs: {k_parallel} -> {k_parallel_value} N/m")
