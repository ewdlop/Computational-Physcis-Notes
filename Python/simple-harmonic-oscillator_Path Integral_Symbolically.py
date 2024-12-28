import sympy as sp

# Define symbolic variables
q, t, m, omega, hbar = sp.symbols('q t m omega hbar')
qi, qf, ti, tf = sp.symbols('qi qf ti tf')
S = sp.Function('S')(q, t)

# Define the Lagrangian for the simple harmonic oscillator
L = (1/2) * m * sp.diff(q, t)**2 - (1/2) * m * omega**2 * q**2

# Define the action as an integral of the Lagrangian
action_integral = sp.integrate(L, (t, ti, tf))

# Substitute the boundary conditions for qi and qf
action_integral = action_integral.subs({q.subs(t, ti): qi, q.subs(t, tf): qf})

# Display the action
print(f"Action S: {action_integral}")

# Now let's assume a simple path and compute the action for that path
# For simplicity, assume a linear path q(t) = qi + (qf - qi) * (t - ti) / (tf - ti)

# Define the linear path
linear_path = qi + (qf - qi) * (t - ti) / (tf - ti)

# Substitute the linear path into the Lagrangian
L_linear = L.subs(sp.diff(q, t), sp.diff(linear_path, t)).subs(q, linear_path)

# Compute the action for the linear path
S_linear = sp.integrate(L_linear, (t, ti, tf))

# Display the action for the linear path
print(f"Action S for linear path: {S_linear}")
