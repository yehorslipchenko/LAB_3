import random
import GeneticAlgorithm
import functions
import matplotlib.pyplot as plt

# constants
import functions

population_size = 15
chrom_length = 2
p_cross = 0.9
p_mut = 0.1
max_gen = 100
func = 1
error = 1e-6
low = -5
up = 5

# Variables for GA
population = GeneticAlgorithm.CreatePopulation(population_size, chrom_length, low, up)
GeneticAlgorithm.Init(population, func)
minFitVal = []
avgFitVal = []
fitnessValues = [individual.fitness.values[0] for individual in population]
GenCount = 0
end_state = 0
if func == 3:
    end_state = -19.2085

# Evolution process
while min(fitnessValues) > end_state and GenCount < max_gen:
    GenCount += 1
    offspring = GeneticAlgorithm.Selection(population, len(population))
    offspring = list(map(GeneticAlgorithm.clone, offspring))

    for first_child, second_child in zip(offspring[::2], offspring[1::2]):
        if random.random() < p_cross:
            GeneticAlgorithm.Crossover(first_child, second_child)

    for mutant in offspring:
        if random.random() < p_mut:
            GeneticAlgorithm.Mutation(mutant, 1.0 / chrom_length)
    if func == 1:
        freshFitnessValues = list(map(functions.Ackley, offspring))
    elif func == 2:
        freshFitnessValues = list(map(functions.Bukin_N6, offspring))
    elif func == 3:
        freshFitnessValues = list(map(functions.Holder, offspring))

    for individual, fitnessValues in zip(offspring, freshFitnessValues):
        individual.fitness.values = fitnessValues

    population[:] = offspring

    fitnessValues = [ind.fitness.values[0] for ind in population]

    minFit = min(fitnessValues)
    avgFit = sum(fitnessValues) / len(population)
    minFitVal.append(minFit)
    avgFitVal.append(avgFit)
    print(f"Gen{GenCount}: MinFit->{minFit} AvgFit->{avgFit}")

    BestCandidate = fitnessValues.index(min(fitnessValues))
    print(f"Best candidate:", *population[BestCandidate], "\n")

plt.plot(minFitVal, color='red')
plt.plot(avgFitVal, color='green')
plt.xlabel('Generation')
plt.ylabel('min/avg fitness')
plt.title('depend min and avg fitness of generations')
plt.show()
