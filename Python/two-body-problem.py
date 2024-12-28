import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
G = 6.67430e-11  # gravitational constant, m^3 kg^-1 s^-2
m1 = 5.972e24    # mass of body 1, kg (example: Earth)
m2 = 7.348e22    # mass of body 2, kg (example: Moon)

def two_body_equations(t, y):
    r1 = y[:2]  # position of body 1
    r2 = y[2:4]  # position of body 2
    v1 = y[4:6]  # velocity of body 1
    v2 = y[6:8]  # velocity of body 2
    
    r = np.linalg.norm(r2 - r1)
    force = G * m1 * m2 / r**3 * (r2 - r1)
    
    dv1dt = force / m1
    dv2dt = -force / m2
    
    return [v1[0], v1[1], v2[0], v2[1], dv1dt[0], dv1dt[1], dv2dt[0], dv2dt[1]]

# Initial conditions: [r1x, r1y, r2x, r2y, v1x, v1y, v2x, v2y]
y0 = [0, 0, 384400000, 0, 0, 0, 0, 1022]  # example values

# Time span
t_span = (0, 28 * 24 * 3600)  # 28 days in seconds
t = np.linspace(0, 28 * 24 * 3600, 1000)

# Solve the system of differential equations
sol = solve_ivp(two_body_equations, t_span, y0, t_eval=t, method='RK45')
r1, r2 = sol.y[:2], sol.y[2:4]

# Animation
fig, ax = plt.subplots()
ax.set_xlim(-2e8, 2e8)
ax.set_ylim(-2e8, 2e8)
line1, = ax.plot([], [], 'bo', markersize=10)  # body 1
line2, = ax.plot([], [], 'ro', markersize=5)  # body 2
trail1, = ax.plot([], [], 'b-', lw=1)
trail2, = ax.plot([], [], 'r-', lw=1)

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    trail1.set_data([], [])
    trail2.set_data([], [])
    return line1, line2, trail1, trail2

def update(frame):
    line1.set_data(r1[0][frame], r1[1][frame])
    line2.set_data(r2[0][frame], r2[1][frame])
    trail1.set_data(r1[0][:frame], r1[1][:frame])
    trail2.set_data(r2[0][:frame], r2[1][:frame])
    return line1, line2, trail1, trail2

ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True)
plt.show()
