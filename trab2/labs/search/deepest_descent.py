from random import randint, shuffle, sample
from common_functions import *

def DeepestDescent(items, max_size, s):
    state, value, size = s, StateValue(s, items), StateSize(s, items)

    while True:
        #Obtem um vizinho aleatorio
        gss = GenerateStates(state)

        control = 0
        for gs in gss:
            if StateSize(gs, items) <= max_size:
                if StateValue(gs, items) > StateValue(state, items):
                    state = gs
                    control = 1

        if control == 0:
            break
    
    return state, StateValue(state, items), StateSize(state, items)

''' MAIN '''
if __name__ == '__main__':
    items = [(1, 3), (4, 6), (5, 7)]
    max_size = 19

    initial_state = GenerateAnyValidState(items, max_size)
    
    states = DeepestDescent(items, max_size, initial_state)
    print(states)