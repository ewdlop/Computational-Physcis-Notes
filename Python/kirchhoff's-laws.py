import sympy as sp

# Define the symbols
I1, I2, I3 = sp.symbols('I1 I2 I3')
R1, R2, R3, E = sp.symbols('R1 R2 R3 E')

# Kirchhoff's Current Law (KCL)
kcl_eq = sp.Eq(I1, I2 + I3)

# Kirchhoff's Voltage Law (KVL) for two loops
kvl_eq1 = sp.Eq(E - I1 * R1 - I2 * R2, 0)
kvl_eq2 = sp.Eq(I2 * R2 - I3 * R3, 0)

# Solve the system of equations
solutions = sp.solve((kcl_eq, kvl_eq1, kvl_eq2), (I1, I2, I3))

# Display the solutions
print(f"Solutions: {solutions}")
