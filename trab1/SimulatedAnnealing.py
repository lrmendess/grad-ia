from math import exp
from time import time
from random import uniform
from Utils import Valor, Tamanho, EhValido, VizinhoAleatorio

def AceitaPior(pior, melhor, temperatura):
    probabilidade = 1 / exp((pior - melhor) / temperatura)

    return probabilidade > uniform(0, 1)

def SimulatedAnnealing(t, vt, tempo_limite, iteracoes, temperatura, alpha):
    tempo = time()
    
    estado = [0] * len(vt)
    aux = [0] * len(vt)

    while temperatura > 0.1:
        if (time() - tempo) >= tempo_limite:
            break

        for _ in range(iteracoes):
            vizinho = VizinhoAleatorio(aux)

            if not EhValido(vizinho, t, vt):
                continue

            if Valor(vizinho, vt) > Valor(aux, vt):
                aux = vizinho

                if Valor(aux, vt) > Valor(estado, vt):
                    estado = aux
            
            elif AceitaPior(Valor(vizinho, vt), Valor(aux, vt), temperatura):
                aux = vizinho
        
        temperatura *= alpha

    tempo = time() - tempo
    
    return estado, Valor(estado, vt), Tamanho(estado, vt), tempo

''' MAIN '''
if __name__ == '__main__':
    vt = [(1, 3), (4, 6), (5, 7)]
    t = 19
    iteracoes = 20
    temperatura = 200
    alpha = 0.05
    tempo_limite = 5.0
    
    resultado = SimulatedAnnealing(t, vt, tempo_limite, iteracoes, temperatura, alpha)
    print(resultado)