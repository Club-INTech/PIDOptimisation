import unittest
from GA.ga_pid import ga_step
from GA.individual_class import Individual
from GA.ga_pid_const import POPULATION, GENERATIONS
from simulator.model import model_output
from GA.sample_lib_utils import *
from logger import logger
import matplotlib.pyplot as pyplot


class GATest(unittest.TestCase):

    def test(self):
        people = [Individual() for _ in range(POPULATION)]
        for i in range(POPULATION):
            s, t = model_output(1, people[i].kp, people[i].ki, people[i].kd)
            people[i].set_s_t(s, t)

        logger_step = GENERATIONS / 20
        file = logger.define_file()
        for i in range(GENERATIONS):

            # errors of the previous best individuals in population
            si, ti = model_output(1, people[0].kp, people[0].ki, people[0].kd)
            stat_err = stat_error(si, 1)
            over = overflow(si, 1)
            t5 = response_time(si, ti)
            abs_err = absolute_error(si, ti, 1)
            prev_err = [stat_err, over, t5, abs_err]
            people = ga_step(people, 1, prev_err, POPULATION)

            for i in range(len(people)):
                s, t = model_output(1, people[i].kp, people[i].ki, people[i].kd)
                people[i].set_s_t(s, t)

            if i % logger_step == 0:
                logger.save_evolution(file, people, 1)

        os, ot = model_output(1, people[0].kp, people[0].ki, people[0].kd)
        pyplot.plot(ot, os)
        pyplot.show()


if __name__ == '__main__':
    unittest.main()
