from GA.sample_lib_utils import *
from GA.individual_class import Individual
from GA.ga_pid_const import *
import random

    
def ga_step(individuals, instruction, previous_error, population=POPULATION):

    individuals = score(individuals, instruction)
    individuals = selection(individuals)
    individuals = adaptiveness(individuals, previous_error, instruction)
    individuals = crossover(individuals, population)
    individuals = mutation(individuals)

    return individuals


def score(individuals, instruction):
    for individual in individuals:
        individual.score = score_mod(individual.s, individual.t, instruction)
    
    return individuals


def selection(individuals):

    individuals = sorted(individuals, key=lambda individual: individual.score, reverse=False)
    individuals = individuals[0:int(SELECTION_RATE * len(individuals))]

    return individuals


def adaptiveness(individuals, previous_error, instruction):
    for individual in individuals:
        stat_err = stat_error(individual.s, instruction)
        over = overflow(individual.s)
        t5 = response_time(individual.s, individual.t)
        abs_err = absolute_error(individual.s, individual.t, instruction)

        kp_change = random.uniform(0.0, MAX_ADAPTIVENESS_CHANGE)
        ki_change = random.uniform(0.0, MAX_ADAPTIVENESS_CHANGE)
        kd_change = random.uniform(0.0, MAX_ADAPTIVENESS_CHANGE)

        stat_err_sign = sign(stat_err, previous_error[0])
        over_sign = sign(over, previous_error[1])
        t5_sign = sign(t5, previous_error[2])
        abs_err = sign(abs_err, previous_error[3])

        kp_score = KP_STAT_ERR_ADAPTIVENESS_RATING * stat_err_sign + KP_OVER_ERR_ADAPTIVENESS_RATING * over_sign + KP_T5_ERR_ADAPTIVENESS_RATING * t5_sign + KP_ABS_ERR_ADAPTIVENESS_RATING * abs_err
        ki_score = KI_STAT_ERR_ADAPTIVENESS_RATING * stat_err_sign + KI_OVER_ERR_ADAPTIVENESS_RATING * over_sign + KI_T5_ERR_ADAPTIVENESS_RATING * t5_sign + KI_ABS_ERR_ADAPTIVENESS_RATING * abs_err
        kd_score = KD_STAT_ERR_ADAPTIVENESS_RATING * stat_err_sign + KD_OVER_ERR_ADAPTIVENESS_RATING * over_sign + KD_T5_ERR_ADAPTIVENESS_RATING * t5_sign + KD_ABS_ERR_ADAPTIVENESS_RATING * abs_err

        individual.kp = individual.kp - (kp_change * kp_score)
        individual.ki = individual.ki - (ki_change * ki_score)
        individual.kd = individual.kd - (kd_change * kd_score)

    return individuals


def sign(err1, err2):
    if err1 - err2 <= EPS:
        return 0
    return (err1 - err2) / abs(err1 - err2)


def crossover(individuals, population):

    offspring = []

    for _ in range((population - len(individuals)) // 2):
        parent1 = random.choice(individuals)
        parent2 = random.choice(individuals)

        importance = random.randint(1, 100)

        child1 = Individual()
        child2 = Individual()

        child1.kp = (importance * parent1.kp + (100-importance) * parent2.kp) / 100
        child2.kp = (importance * parent2.kp + (100-importance) * parent1.kp) / 100
        child1.ki = (importance * parent1.ki + (100-importance) * parent2.ki) / 100
        child2.ki = (importance * parent2.ki + (100-importance) * parent1.ki) / 100
        child1.kd = (importance * parent1.kd + (100-importance) * parent2.kd) / 100
        child2.kd = (importance * parent2.kd + (100-importance) * parent1.kd) / 100

        offspring.append(child1)
        offspring.append(child2)

    individuals.extend(offspring)

    return individuals


def mutation(individuals):
    for individual in individuals:
        if random.uniform(0.0, 1.0) <= MUTATION_CONDITION:
            individual.kp = MUTATION_MULTIPLIER * individual.kp
            individual.ki = MUTATION_MULTIPLIER * individual.ki
            individual.kd = MUTATION_MULTIPLIER * individual.kd

    return individuals
