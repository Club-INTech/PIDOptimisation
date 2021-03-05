import numpy as np

# Dynamic modelisation consts

J = 41.0

# Euler

y0 = np.array([0, 0, 0])
dt = 0.05
simulation_time = 10.0
generated_t = np.linspace(0, simulation_time, dt)


def A(t):
    return t * np.array([[1, 2, 3], [3, 2, 1], [2, 1, 3]])
