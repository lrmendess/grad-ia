from time import time
from random import randint, uniform, choice
from Utils import Valor, Tamanho, EhValido, EstadoAleatorio

def Genetic(t, vt, tempo_limite, iteracoes, tamanho_populacao, taxa_crossover, taxa_mutacao):
    tempo = time()

    estado, valor, tamanho = [0] * len(vt), 0, 0

    populacao = [EstadoAleatorio(t, vt) for _ in range(tamanho_populacao)]

    for _ in range(iteracoes):
        if (time() - tempo) >= tempo_limite:
            break
            
        populacao.sort(key = lambda e: Valor(e, vt), reverse = True)
        gs = populacao.pop(0)

        if Valor(gs, vt) > Valor(estado, vt):
            estado = gs

        futuro = [gs]

        evoluidos = Evolve(populacao, t, vt, tamanho_populacao, taxa_crossover, taxa_mutacao)
        futuro.extend(evoluidos)

        estrangeiros = [EstadoAleatorio(t, vt) for _ in range(tamanho_populacao - len(futuro))]
        futuro.extend(estrangeiros)
        
        populacao = futuro
    
    tempo = time() - tempo

    return estado, Valor(estado, vt), Tamanho(estado, vt), tempo

def Evolve(populacao, t, vt, tamanho_populacao, taxa_crossover, taxa_mutacao):
    evoluidos = Selecao(populacao, vt)
    evoluidos = Crossover(evoluidos, t, vt, taxa_crossover)
    evoluidos = Mutacao(evoluidos, t, vt, taxa_mutacao)
    return evoluidos

def Selecao(populacao, vt):
    limite = len(populacao) // 2

    selecionados = []

    while len(selecionados) < limite:
        roleta = Roleta(populacao, vt)
        
        probabilidade = uniform(0, 1)

        #individual = (ratio, state)
        for individuo in roleta:
            if probabilidade <= individuo[0]:
                selecionados.append(individuo[1])
                populacao.remove(individuo[1])
                break

    return selecionados

def Roleta(populacao, vt):
    maximo = sum([Valor(e, vt) for e in populacao])

    razoes = [(Valor(e, vt) / maximo, e) for e in populacao]
    razoes.sort(key = lambda r: r[0], reverse = True)

    roleta, soma = [], 0
    
    for individuo in razoes:
        soma += individuo[0]
        roleta.append((soma, individuo[1]))

    return roleta

def Crossover(populacao, t, vt, taxa_crossover):
    novatos = []

    reprodutores = [e for e in populacao if uniform(0, 1) <= taxa_crossover]

    for _ in range(len(reprodutores) // 2):
        pai = choice(reprodutores)
        reprodutores.remove(pai)

        mae = choice(reprodutores)
        reprodutores.remove(mae)

        gene = randint(0, len(vt) - 1)

        descendente = pai.copy()
        descendente[gene] = mae[gene]

        if EhValido(descendente, t, vt):
            novatos.append(descendente)

        descendente = mae.copy()
        descendente[gene] = pai[gene]

        if EhValido(descendente, t, vt):
            novatos.append(descendente)

    return novatos

def Mutacao(populacao, t, vt, taxa_mutacao):
    candidatos, mutados = [], []

    for e in populacao:
        if uniform(0, 1) <= taxa_mutacao:
            candidatos.append(e)
        else:
            mutados.append(e)

    for candidato in candidatos:
        gene = randint(0, len(vt) - 1)

        if candidato[gene] == 0:
            candidato[gene] += 1
        else:
            candidato[gene] += choice([-1, 1])

        if EhValido(candidato, t, vt):
            mutados.append(candidato)

    return mutados

''' MAIN '''
if __name__ == '__main__':
    vt = [(1, 3), (4, 6), (5, 7)]
    t = 19
    tamanho_populacao = 10
    iteracoes = 5
    taxa_crossover = 0.5
    taxa_mutacao = 0.1
    tempo_limite = 5.0
    
    resultado = Genetic(t, vt, tempo_limite, iteracoes, tamanho_populacao, taxa_crossover, taxa_mutacao)
    print(resultado)