import math


def Ackley(individual):
    x, y = individual
    f = -20 * math.exp(-0.2 * math.sqrt(0.5 * (math.pow(x, 2) + math.pow(y, 2)))) \
        - math.exp(0.5 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y))) + math.e + 20
    return f,


def Bukin_N6(individual):
    x, y = individual
    f = 100 * math.sqrt(math.fabs(y - 0.01 * math.pow(x, 2))) + 0.01 * math.fabs(x + 10)
    return f,


def Holder(individual):
    x, y = individual
    f = -math.fabs(
        math.sin(x) * math.cos(y) * math.exp(math.fabs(1 - (math.sqrt(math.pow(x, 2) + math.pow(y, 2)) / math.pi))))
    return f,
