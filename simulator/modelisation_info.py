from GA.ga_pid_const import MIN_POINTS_NUMBER
from math import pow

# This file contains modelisation information

# Modelisation constants

POINTS_NUMBER = MIN_POINTS_NUMBER + 2
DELTA_T = 0.25

# Transfer function constants

# M(p)

TAU_E = 20 * pow(10, -4)
TAU = 2.2 * pow(10, -3)
K_0 = 4.2 * pow(10, -2)

# R(p)

J = pow(10, -3)
Wheel_Radius = 0.03
Mass = 5.0
K_1 = 5.86 * pow(10, -4)







