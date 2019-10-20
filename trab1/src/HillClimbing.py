from Utils import Valor, Tamanho, EhValido, VizinhosPositivos

def HillClimbing(t, vt):
    estado = [0] * len(vt)

    while True:
        vizinhos = VizinhosPositivos(estado)
        vizinhos = list(filter(lambda e: EhValido(e, t, vt), vizinhos))
        
        if len(vizinhos) <= 0:
            break

        estado = max(vizinhos, key = lambda e: Valor(e, vt))

    return estado, Valor(estado, vt), Tamanho(estado, vt)

''' MAIN '''
if __name__ == '__main__':
    vt = [(1, 3), (4, 6), (5, 7)]
    t = 19
    
    resultado = HillClimbing(t, vt)
    print(resultado)