from hill_climbing import HillClimbing
from queue import PriorityQueue
from common_functions import *

def OptEstimation(state, items, max_size, is_optimistic = True):
    index = BestReasonIndex(items)
    estimated_state = state.copy()

    while StateSize(estimated_state, items) <= max_size:
        estimated_state[index] += 1

    if is_optimistic:
        estimated_state[index] += 1

    return StateValue(estimated_state, items)

def BranchAndBound(items, max_size, is_optimistic = True):
    state, value, size = HillClimbing(items, max_size)

    queue = PriorityQueue()
    queue.put((0, [0] * len(state)))

    while not queue.empty():
        _, qs = queue.get()
        gss = GenerateIncrementedStates(qs)

        for gs in gss:
            if StateSize(gs, items) <= max_size:
                if OptEstimation(gs, items, max_size, is_optimistic) > value:
                    if StateValue(gs, items) > value:
                        state = gs
                    queue.put((StateValue(gs, items), gs))

    return state, StateValue(state, items), StateSize(state, items)

''' MAIN '''
if __name__ == '__main__':
    items = [(1, 3), (4, 6), (5, 7)]
    max_size = 19
    
    states = BranchAndBound(items, max_size)
    print('Opti Heuristic {0}'.format(states))

    states = BranchAndBound(items, max_size, False)
    print('Pess Heuristic {0}'.format(states))
