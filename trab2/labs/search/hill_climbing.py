from common_functions import *

def HC_BestNextState(state, items, max_size):
    states = GenerateIncrementedStates(state)

    index = 0
    for i in range(0, len(states)):
        if StateSize(states[i], items) <= max_size:
            if StateValue(states[i], items) > StateValue(states[index], items):
                index = i

    return states[index]

def HillClimbing(items, max_size):
    state, value, size = [0] * len(items), 0, 0

    while Fits(state, items, max_size):
        state = HC_BestNextState(state, items, max_size)

    value = StateValue(state, items)
    size = StateSize(state, items)

    return state, value, size

''' MAIN '''
if __name__ == '__main__':
    items = [(1, 3), (4, 6), (5, 7)]
    max_size = 19
    
    states = HillClimbing(items, max_size)
    print(states)
