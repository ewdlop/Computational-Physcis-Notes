import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
G = 6.67430e-11  # gravitational constant, m^3 kg^-1 s^-2
m1 = 1.0e30      # mass of body 1, kg (example: Sun)
m2 = 6.0e24      # mass of body 2, kg (example: Earth)
m3 = 7.0e22      # mass of body 3, kg (example: Moon)

def three_body_equations(t, y):
    r1 = y[:2]  # position of body 1
    r2 = y[2:4]  # position of body 2
    r3 = y[4:6]  # position of body 3
    v1 = y[6:8]  # velocity of body 1
    v2 = y[8:10]  # velocity of body 2
    v3 = y[10:12]  # velocity of body 3
    
    r12 = np.linalg.norm(r2 - r1)
    r13 = np.linalg.norm(r3 - r1)
    r23 = np.linalg.norm(r3 - r2)
    
    F12 = G * m1 * m2 / r12**3 * (r2 - r1)
    F13 = G * m1 * m3 / r13**3 * (r3 - r1)
    F23 = G * m2 * m3 / r23**3 * (r3 - r2)
    
    dv1dt = (F12 + F13) / m1
    dv2dt = (-F12 + F23) / m2
    dv3dt = (-F13 - F23) / m3
    
    return [v1[0], v1[1], v2[0], v2[1], v3[0], v3[1], dv1dt[0], dv1dt[1], dv2dt[0], dv2dt[1], dv3dt[0], dv3dt[1]]

# Initial conditions: [r1x, r1y, r2x, r2y, r3x, r3y, v1x, v1y, v2x, v2y, v3x, v3y]
y0 = [0, 0, 1.5e11, 0, 1.5e11 + 384400000, 0, 0, 0, 0, 29780, 0, 29780 + 1022]

# Time span
t_span = (0, 365.25 * 24 * 3600)  # 1 year in seconds
t = np.linspace(0, 365.25 * 24 * 3600, 1000)

# Solve the system of differential equations
sol = solve_ivp(three_body_equations, t_span, y0, t_eval=t, method='RK45')
r1, r2, r3 = sol.y[:2], sol.y[2:4], sol.y[4:6]

# Animation
fig, ax = plt.subplots()
ax.set_xlim(-2e11, 2e11)
ax.set_ylim(-2e11, 2e11)
line1, = ax.plot([], [], 'yo', markersize=10)  # body 1 (Sun)
line2, = ax.plot([], [], 'bo', markersize=5)   # body 2 (Earth)
line3, = ax.plot([], [], 'ro', markersize=2)   # body 3 (Moon)
trail1, = ax.plot([], [], 'y-', lw=1)
trail2, = ax.plot([], [], 'b-', lw=1)
trail3, = ax.plot([], [], 'r-', lw=1)

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    trail1.set_data([], [])
    trail2.set_data([], [])
    trail3.set_data([], [])
    return line1, line2, line3, trail1, trail2, trail3

def update(frame):
    line1.set_data(r1[0][frame], r1[1][frame])
    line2.set_data(r2[0][frame], r2[1][frame])
    line3.set_data(r3[0][frame], r3[1][frame])
    trail1.set_data(r1[0][:frame], r1[1][:frame])
    trail2.set_data(r2[0][:frame], r2[1][:frame])
    trail3.set_data(r3[0][:frame], r3[1][:frame])
    return line1, line2, line3, trail1, trail2, trail3

ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True)
plt.show()
