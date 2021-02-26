import datetime
from GA.individual_class import Individual
from GA.ga_pid_const import EPS
from GA.sample_lib_utils import *


def define_file(directory_path, test=False):
    date = datetime.datetime.now()
    name = "log_" + str(date).replace(" ", "_").replace(".", "_").replace(":", "-")
    if test:
        name = "test_" + name
    path = directory_path + "/" + name
    file = open(path, 'w')
    return file


def save_evolution(people, instruction, file):
    file.write("_____________________________\n")
    for individual in people:
        save_individual(file, individual, instruction)
    file.write("\n")
    file.write("_____________________________\n")
    file.close()


def save_individual(file, individual, instruction):
    s, t = individual.s, individual.t

    stat_err = stat_error(s, instruction)
    abs_err = absolute_error(s, t, instruction)
    t5 = response_time(s, t)
    over = overflow(s, instruction)

    kp = individual.kp
    ki = individual.ki
    kd = individual.kd

    stability = is_stable(s, EPS)

    file.write("PID : " + str(kp) + " " + str(ki) + " " + str(kd) + " with errors : stat_err - " + str(stat_err)
               + " abs_err - " + str(abs_err) + " response time - " + str(t5) + " over - " + str(over) + " | stable : "
               + str(stability))
