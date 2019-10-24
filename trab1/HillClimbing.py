from time import time
from Utils import Valor, Tamanho, EhValido, VizinhosPositivos

def HillClimbing(t, vt, tempo_limite):
    tempo = time()

    estado = [0] * len(vt)

    while True:
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

        estado = max(vizinhos, key = lambda e: Valor(e, vt))

    tempo = time() - tempo

    return estado, Valor(estado, vt), Tamanho(estado, vt), tempo

''' MAIN '''
if __name__ == '__main__':
    vt = [(1, 3), (4, 6), (5, 7)]
    t = 19
    
    resultado = HillClimbing(t, vt)
    print(resultado)