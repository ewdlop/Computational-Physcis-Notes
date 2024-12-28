import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define the symbols
q, E, m, k = sp.symbols('q E m k')

# Define the integrand
integrand = sp.sqrt(2 * m * E - m * k * q**2)

# Integrate to find W(q)
W_q = sp.integrate(integrand, q)
print(f"W(q) = {W_q}")

# Assigning specific values
m_value = 1  # mass
k_value = 1  # spring constant
E_value = 1  # energy

# Substitute numerical values into W(q)
W_q_numeric = W_q.subs({m: m_value, k: k_value, E: E_value})

# Convert to a numerical function for plotting
W_q_func = sp.lambdify(q, W_q_numeric, 'numpy')

# Generate data for plotting
q_values = np.linspace(-2, 2, 400)
W_values = W_q_func(q_values)

# Plot the result
plt.plot(q_values, W_values, label="W(q)")
plt.xlabel('q')
plt.ylabel('W(q)')
plt.title('Hamilton-Jacobi Solution for a Simple Harmonic Oscillator')
plt.legend()
plt.grid(True)
plt.show()
