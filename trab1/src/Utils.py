from math import ceil
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

def EstadoAleatorio(t, vt):
    maximo = max(vt, key = lambda e: t / e[1])
    maximo = ceil(t / maximo[1])

    estado = sample(range(maximo), len(vt))

    while not EhValido(estado, t, vt):
        estado = sample(range(maximo), len(vt))

    return estado
