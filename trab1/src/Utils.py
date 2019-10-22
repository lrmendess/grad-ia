from math import ceil
from time import time
from random import sample, randint

def Tamanho(estado, vt):
    soma = 0
    
    for i in range(len(estado)):
        soma += estado[i] * vt[i][1]
    
    return soma

def Valor(estado, vt):
    soma = 0

    for i in range(len(estado)):
        soma += estado[i] * vt[i][0]
    
    return soma

def EhValido(estado, t, vt):
    return Tamanho(estado, vt) <= t

def VizinhosPositivos(estado):
    estados = []

    for i in range(len(estado)):
        vizinho = estado.copy()
        vizinho[i] += 1
        estados.append(vizinho)

    return estados

def VizinhosNegativos(estado):
    estados = []

    for i in range(len(estado)):
        if estado[i] > 0:
            vizinho = estado.copy()
            vizinho[i] -= 1
            estados.append(vizinho)

    return estados

def Vizinhos(estado):
    estados = []

    estados.extend(VizinhosNegativos(estado))
    estados.extend(VizinhosPositivos(estado))

    return estados

def VizinhoAleatorio(estado):
    vizinhos = Vizinhos(estado)
    indice = randint(0, len(vizinhos) - 1)

    return vizinhos[indice]

def Arredonda(num):
    if num < 1:
        return 1
    
    return ceil(num)

def EstadoAleatorio(t, vt, tempo, tempo_limite):
    maximos = list(map(lambda e: Arredonda((t / e[1]) * 0.1), vt))

    estado = [0] * len(vt)

    while True:
        # TIMER CHECK
        if (time() - tempo) >= tempo_limite:
            break

        for i in range(len(vt)):
            estado[i] = randint(0, maximos[i])

        if EhValido(estado, t, vt) and Tamanho(estado, vt) > 0:
            break

        estado = [0] * len(vt)

    return estado

def EstadoAleatorio2(t, vt):
    # tempo = time()

    maximo = max(vt, key = lambda e: t / e[1])
    maximo = ceil(t / maximo[1])

    estado = sample(range(maximo), len(vt))

    while not EhValido(estado, t, vt):
        estado = sample(range(maximo), len(vt))

    # print(time() - tempo)

    return estado