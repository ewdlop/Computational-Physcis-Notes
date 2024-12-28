import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Constants
m1, m2 = 1.0, 1.0  # masses
l1, l2 = 1.0, 1.0  # lengths
g = 9.81  # acceleration due to gravity

# Equations of motion derived from the Euler-Lagrange equation
def equations_of_motion(t, state):
    theta1, z1, theta2, z2 = state
    c, s = np.cos(theta1 - theta2), np.sin(theta1 - theta2)
    
    theta1_dot = z1
    z1_dot = (m2 * g * np.sin(theta2) * c - m2 * s * (l1 * z1**2 * c + l2 * z2**2) - (m1 + m2) * g * np.sin(theta1)) / \
             (l1 * (m1 + m2 * s**2))
    
    theta2_dot = z2
    z2_dot = ((m1 + m2) * (l1 * z1**2 * s - g * np.sin(theta2) + g * np.sin(theta1) * c) + m2 * l2 * z2**2 * s * c) / \
             (l2 * (m1 + m2 * s**2))
    
    return [theta1_dot, z1_dot, theta2_dot, z2_dot]

# Initial conditions: [theta1, z1, theta2, z2]
initial_conditions = [np.pi / 2, 0, np.pi / 2, 0]

# Time span for the simulation
t_span = (0, 10)
t_eval = np.linspace(*t_span, 1000)

# Solving the ODE
solution = solve_ivp(equations_of_motion, t_span, initial_conditions, t_eval=t_eval, method='RK45')

# Plotting the results
theta1, theta2 = solution.y[0], solution.y[2]

x1 = l1 * np.sin(theta1)
y1 = -l1 * np.cos(theta1)
x2 = x1 + l2 * np.sin(theta2)
y2 = y1 - l2 * np.cos(theta2)

plt.figure()
plt.plot(x1, y1, label='Mass 1')
plt.plot(x2, y2, label='Mass 2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Double Pendulum Simulation')
plt.legend()
plt.show()
