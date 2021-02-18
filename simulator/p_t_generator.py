import random


def generate_p(points_number):
    p = [random.uniform(0.01, 0.05)]
    for i in range(points_number - 1):
        p.append(random.uniform(p[i] + 0.02, p[i] + 0.06))
    return p


def generate_t(points_number, dt):
    t = [(i+1) * dt for i in range(points_number)]
    return t
