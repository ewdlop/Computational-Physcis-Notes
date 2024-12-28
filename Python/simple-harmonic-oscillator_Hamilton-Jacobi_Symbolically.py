import sympy as sp

# Define symbolic variables
q, p, t, m, k, E = sp.symbols('q p t m k E')
S = sp.Function('S')(q, t)

# Define the Hamiltonian for a simple harmonic oscillator
H = p**2 / (2 * m) + (1 / 2) * k * q**2

# Hamilton-Jacobi equation: H + ∂S/∂t = 0
HJ_eq = sp.Eq(H.subs(p, sp.diff(S, q)) + sp.diff(S, t), 0)

# Assume a solution of the form S(q, t) = W(q) - E*t
W = sp.Function('W')(q)
S_sol = W - E * t

# Substitute into the Hamilton-Jacobi equation and solve
HJ_eq_sub = HJ_eq.subs(S, S_sol).doit()
W_sol = sp.solve(HJ_eq_sub, sp.diff(W, q)**2)[0]
W_integral = sp.integrate(sp.sqrt(W_sol), q)

# Display the solution for W(q)
print(f"W(q) = {W_integral}")

# Complete solution S(q, t)
S_complete = W_integral - E * t
print(f"S(q, t) = {S_complete}")
