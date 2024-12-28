import numpy as np
import matplotlib.pyplot as plt
from scipy.special import beta

# Constants
alpha_s = 0.118  # Strong coupling constant at Z boson mass scale

# Simplified PDF model (e.g., for a quark in a proton)
def parton_distribution(x, A=1.0, B=2.0, C=3.0):
    """
    Parametric form of a parton distribution function (PDF).
    x: momentum fraction
    A, B, C: parameters for the PDF model
    """
    return A * x**B * (1 - x)**C

# Generate x values (momentum fraction)
x_values = np.linspace(0.01, 0.99, 100)

# Calculate PDF values for these x values
pdf_values = parton_distribution(x_values)

# Plot the PDF
plt.plot(x_values, pdf_values, label='PDF')
plt.xlabel('Momentum fraction x')
plt.ylabel('PDF f(x)')
plt.title('Simplified Parton Distribution Function')
plt.legend()
plt.grid(True)
plt.show()
