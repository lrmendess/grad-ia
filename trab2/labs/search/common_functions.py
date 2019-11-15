from random import randint, sample
from math import ceil

''' Dado um estado, verifica se eh possivel adicionar mais algum
item sem estourar o limite de tamanho suportado. '''
def Fits(state, items, max_size):
    for i in range(0, len(state)):
        if StateSize(state, items) + items[i][1] <= max_size:
            return True

    return False

''' Dado um estado, gera os possiveis vizinhos incrementados dele. '''
def GenerateIncrementedStates(state):
    states = []

    for i in range(0, len(state)):
        candidate_state = state.copy()
        candidate_state[i] += 1
        states.append(candidate_state)

    return states

''' Dado um estado, gera os possiveis vizinhos decrementados dele. '''
def GenerateDecrementedStates(state):
    states = []

    for i in range(0, len(state)):
        if state[i] > 0:
            candidate_state = state.copy()
            candidate_state[i] -= 1
            states.append(candidate_state)

    return states

''' Dado um estado, gera os possiveis vizinhos incrementados e decrementados dele. '''
def GenerateStates(state):
    gs = []

    gs.extend(GenerateIncrementedStates(state))
    gs.extend(GenerateDecrementedStates(state))

    return gs

''' Dado um estado, gera um unico vizinho aleatorio dele. '''
def GenerateRandomState(state):
    random_state = GenerateStates(state)

    if len(random_state) > 0:
        random_index = randint(0, len(random_state) - 1)
        return random_state[random_index]

    return []

''' Gera um estado valido qualquer de todo o problema '''
def GenerateAnyValidState(items, max_size):
    max_range = max(items, key = lambda x: max_size / x[1])
    max_range = ceil(max_size / max_range[1])

    state = sample(range(max_range), len(items))
    while StateSize(state, items) > max_size:
        state = sample(range(max_range), len(items))

    return state

''' Retorna o indice do item de melhor razao '''
def BestReasonIndex(items):
    index, opt_value = 0, 0

    for i in range(len(items)):
        evaluate = items[i][0] / items[i][1]

        if evaluate > opt_value:
            index = i
            opt_value = evaluate

    return index

''' Fornece o tamanho da mochila '''
def StateSize(state, items):
    sum_ = 0
    
    for i in range(0, len(state)):
        sum_ += state[i] * items[i][1]
    
    return sum_

''' Fornece o valor da mochila '''
def StateValue(state, items):
    sum_ = 0

    for i in range(0, len(state)):
        sum_ += state[i] * items[i][0]
    
    return sum_
