import random
from ga_pid_const import MAX_SCORE, MAX_KD, MAX_KI, MAX_KP


class Individual:

    def __init__(self):
        self.score = MAX_SCORE
        self.s = []
        self.t = []
        self.kp = random.uniform(0.0, 1.0) * MAX_KP
        self.ki = random.uniform(0.0, 1.0) * MAX_KI
        self.kd = random.uniform(0.0, 1.0) * MAX_KD

    def __str__(self):
        return "This individual: " + str(self.kp) + " " + str(self.ki) + " " + str(self.kd)

    def set_s_t(self, s, t):
        self.s = s[:]
        self.t = t[:]
