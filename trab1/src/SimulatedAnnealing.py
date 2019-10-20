from math import exp
from random import uniform
from Utils import Valor, Tamanho, EhValido, VizinhoAleatorio

def AceitaPior(pior, melhor, temperatura):
    probabilidade = 1 / exp((pior - melhor) / temperatura)

    return probabilidade > uniform(0, 1)

def SimulatedAnnealing(t, vt, iteracoes, temperatura, alpha):
    aux = [0] * len(vt)

    while temperatura > 0.1:
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
    
    return estado, Valor(estado, vt), Tamanho(estado, vt)

''' MAIN '''
if __name__ == '__main__':
    vt = [(1, 3), (4, 6), (5, 7)]
    t = 19
    iteracoes = 20
    temperatura = 200
    alpha = 0.05
    
    resultado = SimulatedAnnealing(t, vt, iteracoes, temperatura, alpha)
    print(resultado)