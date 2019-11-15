from math import exp
from random import uniform
from common_functions import GenerateRandomState, StateValue, StateSize

def AcceptWorse(worse, better, t):
    prob = 1 / exp((worse - better) / t)

    return prob > uniform(0, 1)

def SimulatedAnnealing(items, max_size, max_iter, t, alpha):
    state, value, size = [0] * len(items), 0, 0

    init = [0] * len(items)

    while t > 0.1:
        for _ in range(0, max_iter):
            gs = GenerateRandomState(init)

            if StateValue(gs, items) > StateValue(init, items) and StateSize(gs, items) <= max_size:
                init = gs

                if StateValue(init, items) > StateValue(state, items):
                    state = init
            
            elif AcceptWorse(StateValue(gs, items), StateValue(init, items), t) and StateSize(gs, items) <= max_size:
                init = gs
        
        t *= alpha

    value = StateValue(state, items)
    size = StateSize(state, items)
    
    return state, value, size


''' INPUT '''
items = [(1, 3), (4, 6), (5, 7)]
max_size = 19

''' OUTPUT '''
states = SimulatedAnnealing(items, max_size, 20, 200, 0.05)
print(states)
