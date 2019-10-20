from Utils import Valor, Tamanho, EhValido, VizinhosPositivos, EstadoAleatorio
from random import randint, shuffle, sample

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

''' MAIN '''
if __name__ == '__main__':
    vt = [(1, 3), (4, 6), (5, 7)]
    t = 19
    
    inicio = EstadoAleatorio(t, vt)

    resultado = DeepestDescent(t, vt, inicio)
    print(resultado)