from queue import Queue
from common_functions import *

def BS_BestStates(states, items, max_size, m):
    states = list(filter(lambda s: StateSize(s, items) <= max_size, states))
    states.sort(key = lambda s: StateValue(s, items), reverse = True)

    return states[:m]

def BeamSearch(items, max_size, m):
    state, value, size = [0] * len(items), 0, 0
    states, ms = None, None
    
    queue = Queue()
    queue.put(state)

    while not queue.empty():
        states = ms

        ms = []

        for _ in range(queue.qsize()):
            qs = queue.get()
            ms.extend(GenerateIncrementedStates(qs))
        
        ms = BS_BestStates(ms, items, max_size, m)

        [queue.put(s) for s in ms]

    if (states is None) or (len(states) <= 0):
        return [], 0, 0

    state = states[0]
    value = StateValue(state, items)
    size = StateSize(state, items)

    return state, value, size

''' MAIN '''
if __name__ == '__main__':
    items = [(1, 3), (4, 6), (5, 7)]
    max_size = 19
    
    states = BeamSearch(items, max_size, 2)
    print(states)
