from random import randint, shuffle
from common_functions import *

def SimpleDescent(items, max_size, s):
    state, value, size = s, StateValue(s, items), StateSize(s, items)

    while True:
        # Gera os estados vizinhos
        gs = GenerateStates(state)

        #Array de inteiros 0 .. len(gs) desordenado
        random_array = [num for num in range(len(gs))]
        shuffle(random_array)

        control = 0
        for i in range(len(gs)):
            #Obtem um vizinho aleatorio
            r_num = random_array[i]
            gsr = gs[r_num]

            if StateSize(gsr, items) <= max_size:
                if StateValue(gsr, items) > StateValue(state, items):
                    state = gsr
                    control = 1
                    break

        if control == 0:
            break
    
    return state, StateValue(state, items), StateSize(state, items)

''' MAIN '''
if __name__ == '__main__':
    items = [(1, 3), (4, 6), (5, 7)]
    max_size = 19
    
    initial_state = GenerateAnyValidState(items, max_size)

    states = SimpleDescent(items, max_size, initial_state)
    print(states)