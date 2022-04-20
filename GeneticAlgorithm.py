import random
import functions
import math


class FitnessMin():
    def __init__(self):
        self.values = [0]


class Individual(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.fitness = FitnessMin()


def CreateInd(chrom_length, low, up):
    return Individual([random.uniform(low, up) for i in range(chrom_length)])


def CreatePopulation(size=0, chrom_length=2, low=-10, up=5):
    return list([CreateInd(chrom_length, low, up) for i in range(size)])


def clone(value):
    individual = Individual(value[:])
    individual.fitness.values[0] = value.fitness.values[0]
    return individual


def Selection(population, p_size):
    offspring = []
    for i in range(p_size):
        i1 = i2 = i3 = 0
        while i1 == i2 or i1 == i3 or i2 == i3:
            i1, i2, i3 = random.randint(0, p_size - 1), random.randint(0, p_size - 1), random.randint(
                0, p_size - 1)
        offspring.append(min([population[i1], population[i2], population[i3]], key=lambda x: x.fitness.values[0]))
    return offspring


def Crossover(first_child, second_child):
    # s = random.randint(2, len(first_child) - 3)
    s = random.randint(0, 2)
    first_child[s:], second_child[s:] = second_child[s:], first_child[s:]


def Mutation(individual, indpb):
    for i in range(len(individual)):
        if random.random() < indpb:
            individual[i] += random.uniform(-2.5, 2.5)


def Init(population, func):
    if func == 1:
        fitnessValues = list(map(functions.Ackley, population))
    elif func == 2:
        fitnessValues = list(map(functions.Bukin_N6, population))
    elif func == 3:
        fitnessValues = list(map(functions.Holder, population))


    for individual, fitnessValues in zip(population, fitnessValues):
        individual.fitness.values = fitnessValues
