from common_functions import *
from deepest_descent import DeepestDescent

def Multistart(items, max_size, max_iter):
    state, value, size = [0] * len(items), 0, 0

    for i in range(max_iter):
        random_state = GenerateAnyValidState(items, max_size)
        ss, ss_value, ss_size = DeepestDescent(items, max_size, random_state)

        if ss_size <= max_size and ss_value > value:
            state = ss
            value = ss_value
            size = ss_size

    return state, value, size

''' MAIN '''
if __name__ == '__main__':
    items = [(1, 3), (4, 6), (5, 7)]
    max_size = 19
    
    states = Multistart(items, max_size, 10)
    print(states)
