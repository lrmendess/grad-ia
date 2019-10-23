from time import time
from random import choice, uniform, randint, shuffle, sample
from Utils import Valor, Tamanho, EhValido, VizinhosPositivos

def GreedyRandomConstruct(t, vt, m, tempo, tempo_limite):
    greedy = HillClimbing(t, vt, m, tempo, tempo_limite)
    return greedy[0]

def HillClimbing(t, vt, m, tempo, tempo_limite):
    estado = [0] * len(vt)

    while Tamanho(estado, vt) < (t // 2):
        # TIMER CHECK
        if (time() - tempo) >= tempo_limite:
            break

        vizinhos = VizinhosPositivos(estado)

        # TIMER CHECK
        if (time() - tempo) >= tempo_limite:
            break

        vizinhos = list(filter(lambda e: EhValido(e, t, vt), vizinhos))
        
        # TIMER CHECK
        if (time() - tempo) >= tempo_limite:
            break

        if len(vizinhos) <= 0:
            break

        vizinhos.sort(key = lambda e: Valor(e, vt), reverse=True)

        # TIMER CHECK
        if (time() - tempo) >= tempo_limite:
            break
        
        estado = Roleta(vizinhos[:m], vt, tempo, tempo_limite)

        # TIMER CHECK
        if (time() - tempo) >= tempo_limite:
            break

    return estado, Valor(estado, vt), Tamanho(estado, vt)

def Roleta(estados, vt, tempo, tempo_limite):
    maximo = sum([Valor(e, vt) for e in estados])
    
    # TIMER CHECK
    if (time() - tempo) >= tempo_limite:
        return choice(estados)

    razoes = [(Valor(e, vt) / maximo, e) for e in estados]

    # TIMER CHECK
    if (time() - tempo) >= tempo_limite:
        return choice(estados)

    razoes.sort(key = lambda r: r[0], reverse = True)
        
    # TIMER CHECK
    if (time() - tempo) >= tempo_limite:
        return choice(estados)
    
    roleta, soma = [], 0
    
    for individuo in razoes:
        # TIMER CHECK
        if (time() - tempo) >= tempo_limite:
            return choice(estados)

        soma += individuo[0]
        roleta.append((soma, individuo[1]))
            
    probabilidade = uniform(0, 1)

    for individuo in roleta:
        # TIMER CHECK
        if (time() - tempo) >= tempo_limite:
            return choice(roleta)[1]

        if probabilidade <= individuo[0]:
            return individuo[1]

    return choice(estados)

def DeepestDescent(t, vt, inicio, tempo, tempo_limite):
    estado = inicio

    while True:
        # TIMER CHECK
        if (time() - tempo) >= tempo_limite:
            break

        vizinhos = VizinhosPositivos(estado)

        # TIMER CHECK
        if (time() - tempo) >= tempo_limite:
            break

        vizinhos = list(filter(lambda e: EhValido(e, t, vt), vizinhos))

        # TIMER CHECK
        if (time() - tempo) >= tempo_limite:
            break

        continuar = False

        for vizinho in vizinhos:
            # TIMER CHECK
            if (time() - tempo) >= tempo_limite:
                break

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
        # TIMER CHECK
        if (time() - tempo) >= tempo_limite:
            break

        candidato = GreedyRandomConstruct(t, vt, m, tempo, tempo_limite)

        # TIMER CHECK
        if (time() - tempo) >= tempo_limite:
            break

        candidato = DeepestDescent(t, vt, candidato, tempo, tempo_limite)

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