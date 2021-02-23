import datetime
from GA.individual_class import Individual
from GA.ga_pid_const import EPS
from GA.sample_lib_utils import *


def define_file():
    date = datetime.datetime.now()
    file = open("./logs/" + date + ".txt", "w")
    return file


def save_evolution(file, people, instruction):
    file.write("_____________________________\n")
    for individual in people:
        save_individual(file, individual, instruction)
    file.write("\n")
    file.write("_____________________________\n")


def save_individual(file, individual, instruction):
    s, t = individual.s, individual.t

    stat_err = stat_error(s, instruction)
    abs_err = absolute_error(s, t, instruction)
    t5 = response_time(s, t)
    over = overflow(s)

    kp = individual.kp
    ki = individual.ki
    kd = individual.kd

    stability = is_stable(s, EPS)

    file.write("PID : " + str(kp) + " " + str(ki) + " " + str(kd))
