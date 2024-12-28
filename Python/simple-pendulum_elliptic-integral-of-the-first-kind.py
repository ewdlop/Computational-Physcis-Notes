import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.special import ellipk

# Define constants
g = 9.81  # acceleration due to gravity, m/s^2
L = 1.0   # length of the pendulum, m
theta0 = np.pi / 4  # initial angle, radians

# Calculate the period of the pendulum using the complete elliptic integral of the first kind
def period(theta0):
    k = np.sin(theta0 / 2)
    K = ellipk(k**2)
    T = 4 * np.sqrt(L / g) * K
    return T

# Calculate the time points for one full period
T = period(theta0)
t = np.linspace(0, T, 1000)

# Calculate the angular displacement as a function of time using the Jacobi elliptic functions
def theta(t, theta0):
    k = np.sin(theta0 / 2)
    omega = np.sqrt(g / L)
    sn, cn, dn, ph = ellipj(omega * t, k**2)
    return 2 * np.arcsin(k * sn)

# Calculate the angular displacement over time
theta_t = theta(t, theta0)

# Convert to Cartesian coordinates for plotting
x = L * np.sin(theta_t)
y = -L * np.cos(theta_t)

# Animation
fig, ax = plt.subplots()
ax.set_xlim(-L, L)
ax.set_ylim(-L, L)
line, = ax.plot([], [], 'o-', lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    line.set_data([0, x[frame]], [0, y[frame]])
    return line,

ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True)
plt.show()
