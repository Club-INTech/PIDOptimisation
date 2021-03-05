import numpy as np
from scipy import linalg
from math import exp
from inverse_laplace_simulator.modelisation_info import POINTS_NUMBER, DELTA_T
from inverse_laplace_simulator.tranfer import S_p
from inverse_laplace_simulator.p_t_generator import *

p = generate_p(POINTS_NUMBER)
t = generate_t(POINTS_NUMBER, DELTA_T)


def model_output(V0, Kp, Ki, Kd):
    s = np.dot(inverse_solution_matrix(p, t), S_vector(V0, p, Kp, Ki, Kd))
    return s, t


def inverse_solution_matrix(p, t):
    n = len(t)
    matrix = []
    for i in range(n):
        tmp_arr = []
        for j in range(n-1):
            tmp_arr.append(DELTA_T * exp(p[i] * (-1) * t[j]))
        tmp_arr.append((DELTA_T + (1 / p[i])) * exp(p[i] * (-1) * t[n-1]))
        matrix.append(tmp_arr)
    return linalg.inv(np.array(matrix))


def S_vector(V0, p, Kp, Ki, Kd):
    vector = [S_p(V0, p_i, Kp, Ki, Kd) for p_i in p]
    return np.array(vector)
