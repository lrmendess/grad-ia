from time import time
from queue import Queue
from Utils import Valor, Tamanho, EhValido, VizinhosPositivos

def BeamSearch(t, vt, tempo_limite, m):
    tempo = time()

    estado = [0] * len(vt)

    fila = Queue()
    fila.put(estado)

    while True:
        if (time() - tempo) >= tempo_limite:
            break

        expandidos = []

        for _ in range(fila.qsize()):
            vizinhos = VizinhosPositivos(fila.get())
            vizinhos = list(filter(lambda e: EhValido(e, t, vt), vizinhos))
            expandidos.extend(vizinhos)

        if len(expandidos) <= 0:
            break
 
        expandidos.sort(key = lambda e: Valor(e, vt), reverse = True)
        melhores = expandidos[:m]

        [fila.put(e) for e in melhores]

    estado = melhores[0]

    tempo = time() - tempo

    return estado, Valor(estado, vt), Tamanho(estado, vt), tempo

''' MAIN '''
if __name__ == '__main__':
    vt = [(1, 3), (4, 6), (5, 7)]
    t = 19
    m = 2
    tempo_limite = 5.0
    
    resultado = BeamSearch(t, vt, tempo_limite, m)
    print(resultado)