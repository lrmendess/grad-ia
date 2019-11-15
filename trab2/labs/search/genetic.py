from random import randint, shuffle, uniform
from common_functions import *

def Genetic(items, max_size, max_iter, size_pop, crossover_ratio, mutattion_ratio, m):
    state, value, size = [0] * len(items), 0, 0

    population = [GenerateAnyValidState(items, max_size) for _ in range(size_pop)]

    for _ in range(max_iter):
        population.sort(key = lambda s: StateValue(s, items), reverse = True)
        gs = population.pop(0)

        if StateValue(gs, items) > StateValue(state, items):
            state = gs

        future = [gs]

        evolved = Evolve(population, items, max_size, size_pop, crossover_ratio, mutattion_ratio, m)
        future.extend(evolved)

        foreigners = [GenerateAnyValidState(items, max_size) for _ in range(size_pop - len(future))]
        future.extend(foreigners)
        
        population = future
    
    return state, StateValue(state, items), StateSize(state, items)

def Evolve(population, items, max_size, size_pop, crossover_ratio, mutattion_ratio, m):
    return []

def Select(population, items, max_size, max_pop, m):
    selecteds = []

    while len(selecteds) < m:
        if len(population) <= 0:
            return selecteds
        
        roulette = Roulette(population, items, m)
        
        prob = uniform(0, 1)

        #individual = (ratio, state)
        for individual in roulette:
            if prob <= individual[0]:
                selecteds.append(individual[1])
                population.remove(individual[1])
                break

    return selecteds

def Roulette(population, items, m):
    max_values = sum([StateValue(p, items) for p in population])

    if max_values == 0:
        return population[:m]

    roulette = [(StateValue(p, items) / max_values, p) for p in population]
    roulette.sort(key = lambda r: r[0], reverse = True)

    return roulette

def Crossover(population, items, max_size, max_pop, crossover_ratio, m):
    pass

def Mutation(population, items, max_size, max_pop, mutattion_ratio, m):
    pass

''' MAIN '''
if __name__ == '__main__':
    items = [(1, 3), (4, 6), (5, 7)]
    max_size = 19
    size_population = 10
    max_iter = 10
    crossover_ratio = 0.5
    mutattion_ratio = 0.1
    m = 3    
    
    state = Genetic(items, max_size, max_iter, size_population, crossover_ratio, mutattion_ratio, m)
    print(state)