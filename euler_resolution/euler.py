import numpy as np
from euler_resolution.euler_model_consts import dt, A, y0, generated_t


def euler(initial_vector=y0, pass_function=A, interval=dt, t=generated_t):
    s = initial_vector[:]
    for i in range(1, len(t)):
        s = s + interval * np.dot(pass_function(t[i]),s)

    return s, t






