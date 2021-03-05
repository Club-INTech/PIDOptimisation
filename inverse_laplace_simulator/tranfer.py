from inverse_laplace_simulator.modelisation_info import *


def S_p (V0, p, Kp, Ki, Kd):
    return V0 / (p + (p/(C(p, Kp, Ki, Kd) * R(p) * M(p))))


def C(p, Kp, Ki, Kd):
    return (1 + Kp * Ki * p + Kd * Ki * p * p) / (Ki * p)


def R(p):
    return (p * (J / (Wheel_Radius * K_1))) / (1 + p * (Mass / K_1))


def M(p):
    return K_0 / (1 + p * (TAU + TAU_E) + TAU_E * TAU * p * p)

