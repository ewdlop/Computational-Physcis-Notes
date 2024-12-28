import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
g = 9.81  # acceleration due to gravity (m/s^2)
l = 1.0   # length of the pendulum (m)
m = 1.0   # mass of the pendulum (kg)

# Hamiltonian equations
def hamiltonian(t, y):
    theta, p_theta = y
    dtheta_dt = p_theta / (m * l**2)
    dp_theta_dt = -m * g * l * np.sin(theta)
    return [dtheta_dt, dp_theta_dt]

# Initial conditions
theta0 = np.pi / 4  # initial angle (radians)
p_theta0 = 0.0      # initial angular momentum
y0 = [theta0, p_theta0]

# Time span
t_span = (0, 10)  # 10 seconds
t_eval = np.linspace(0, 10, 1000)

# Solve the differential equations
sol = solve_ivp(hamiltonian, t_span, y0, t_eval=t_eval, method='RK45')

# Extract the solutions
theta = sol.y[0]
p_theta = sol.y[1]

# Convert to Cartesian coordinates for visualization
x = l * np.sin(theta)
y = -l * np.cos(theta)

# Plot the pendulum motion
plt.figure(figsize=(10, 5))
plt.plot(t_eval, theta, label='Angle (theta)')
plt.plot(t_eval, p_theta, label='Angular Momentum (p_theta)')
plt.xlabel('Time (s)')
plt.ylabel('Values')
plt.legend()
plt.title('Simple Pendulum: Hamiltonian Mechanics')
plt.show()
