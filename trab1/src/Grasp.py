from time import time
from random import choice, uniform, randint, shuffle, sample
from Utils import Valor, Tamanho, EhValido, VizinhosPositivos, EstadoAleatorio

def GreedyRandomConstruct(t, vt, m):
    greedy = HillClimbing(t, vt, m)
    return greedy[0]

def HillClimbing(t, vt, m):
    estado = [0] * len(vt)

    while Tamanho(estado, vt) < (t // 2):
        vizinhos = VizinhosPositivos(estado)
        vizinhos = list(filter(lambda e: EhValido(e, t, vt), vizinhos))
        
        if len(vizinhos) <= 0:
            break

        vizinhos.sort(key = lambda e: Valor(e, vt), reverse=True)
        
        estado = Roleta(vizinhos[:m], vt)

    return estado, Valor(estado, vt), Tamanho(estado, vt)

def Roleta(estados, vt):
    maximo = sum([Valor(e, vt) for e in estados])
    
    if maximo == 0:
        return estados

    razoes = [(Valor(e, vt) / maximo, e) for e in estados]
    razoes.sort(key = lambda r: r[0], reverse = True)
    
    roleta, soma = [], 0
    
    for individuo in razoes:
        soma += individuo[0]
        roleta.append((soma, individuo[1]))
            
    probabilidade = uniform(0, 1)

    for individuo in roleta:
        if probabilidade <= individuo[0]:
            return individuo[1]

    return choice(estados)

def DeepestDescent(t, vt, inicio):
    estado = inicio

    while True:
        vizinhos = VizinhosPositivos(estado)
        vizinhos = list(filter(lambda e: EhValido(e, t, vt), vizinhos))

        continuar = False

        for vizinho in vizinhos:
            if Valor(vizinho, vt) > Valor(estado, vt):
                estado = vizinho
                continuar = True

        if not continuar:
            break

    return estado, Valor(estado, vt), Tamanho(estado, vt)

def Grasp(t, vt, tempo_limite, iteracoes, m):
    tempo = time()

    estado = [0] * len(vt)

    for _ in range(iteracoes):
        if (time() - tempo) >= tempo_limite:
            break

        candidato = GreedyRandomConstruct(t, vt, m)
        candidato = DeepestDescent(t, vt, candidato)

        # candidato (estado, valor, tamanho)
        if candidato[1] > Valor(estado, vt):
            estado = candidato[0]

    tempo = time() - tempo

    return estado, Valor(estado, vt), Tamanho(estado, vt), tempo

''' MAIN '''
if __name__ == '__main__':
    vt = [(1, 3), (4, 6), (5, 7)]
    t = 19
    iteracoes = 5
    m = 2
    tempo_limite = 5.0
    
    resultado = Grasp(t, vt, tempo_limite, iteracoes, m)
    print(resultado)