import math
import matplotlib.pyplot as plt

def calculate_trajectory(v0, angle, g=9.81):
    """
    Calculate the trajectory of a projectile.
    
    Parameters:
    v0 (float): Initial velocity (m/s)
    angle (float): Launch angle (degrees)
    g (float): Acceleration due to gravity (m/s^2)

    Returns:
    list of tuples: (time, x, y) positions of the projectile
    """
    angle_rad = math.radians(angle)
    t_max = (2 * v0 * math.sin(angle_rad)) / g
    t_values = [t * 0.01 for t in range(int(t_max * 100) + 1)]
    trajectory = []

    for t in t_values:
        x = v0 * t * math.cos(angle_rad)
        y = v0 * t * math.sin(angle_rad) - 0.5 * g * t**2
        trajectory.append((t, x, y))

    return trajectory

# Parameters
initial_velocity = 20  # m/s
launch_angle = 45      # degrees

# Calculate trajectory
trajectory = calculate_trajectory(initial_velocity, launch_angle)

# Extract time, x and y values for plotting
time_values = [point[0] for point in trajectory]
x_values = [point[1] for point in trajectory]
y_values = [point[2] for point in trajectory]

# Plot trajectory
plt.plot(x_values, y_values)
plt.title('Projectile Motion')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.grid()
plt.show()
