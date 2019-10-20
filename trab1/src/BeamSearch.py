from Utils import Valor, Tamanho, EhValido, VizinhosPositivos
from queue import Queue

def BeamSearch(t, vt, m):
    estado = [0] * len(vt)

    fila = Queue()
    fila.put(estado)

    while True:
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

    return estado, Valor(estado, vt), Tamanho(estado, vt)

''' MAIN '''
if __name__ == '__main__':
    vt = [(1, 3), (4, 6), (5, 7)]
    t = 19
    m = 2
    
    resultado = BeamSearch(t, vt, m)
    print(resultado)