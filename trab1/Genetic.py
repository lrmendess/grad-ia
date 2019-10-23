from time import time
from random import randint, uniform, choice
from Utils import Valor, Tamanho, EhValido, EstadoAleatorio

def Genetic(t, vt, tempo_limite, iteracoes, tamanho_populacao, taxa_crossover, taxa_mutacao):
    tempo = time()

    estado, valor, tamanho = [0] * len(vt), 0, 0

    populacao = [EstadoAleatorio(t, vt, tempo, tempo_limite) for _ in range(tamanho_populacao)]

    for _ in range(iteracoes):
        if (time() - tempo) >= tempo_limite:
            break
        
        populacao.sort(key = lambda e: Valor(e, vt), reverse = True)
        gs = populacao.pop(0)

        if Valor(gs, vt) > Valor(estado, vt):
            estado = gs

        # TIMER CHECK
        if (time() - tempo) >= tempo_limite:
            break

        futuro = [gs]

        evoluidos = Evolve(populacao, t, vt, tamanho_populacao, taxa_crossover, taxa_mutacao, tempo, tempo_limite)
        futuro.extend(evoluidos)
        
        # TIMER CHECK
        if (time() - tempo) >= tempo_limite:
            break

        estrangeiros = [EstadoAleatorio(t, vt, tempo, tempo_limite) for _ in range(tamanho_populacao - len(futuro))]
        futuro.extend(estrangeiros)

        # TIMER CHECK
        if (time() - tempo) >= tempo_limite:
            break
        
        populacao = futuro
    
    tempo = time() - tempo

    return estado, Valor(estado, vt), Tamanho(estado, vt), tempo

def Evolve(populacao, t, vt, tamanho_populacao, taxa_crossover, taxa_mutacao, tempo, tempo_limite):
    evoluidos = Selecao(populacao, vt, tempo, tempo_limite)
    
    # TIMER CHECK
    if (time() - tempo) >= tempo_limite:
        return evoluidos
    
    evoluidos = Crossover(evoluidos, t, vt, taxa_crossover, tempo, tempo_limite)
    
    # TIMER CHECK
    if (time() - tempo) >= tempo_limite:
        return evoluidos
    
    evoluidos = Mutacao(evoluidos, t, vt, taxa_mutacao, tempo, tempo_limite)

    return evoluidos

def Selecao(populacao, vt, tempo, tempo_limite):
    limite = len(populacao) // 2

    selecionados = []

    while len(selecionados) < limite:
        # TIMER CHECK
        if (time() - tempo) >= tempo_limite:
            break

        roleta = Roleta(populacao, vt, tempo, tempo_limite)

        selecionados.append(roleta)
        populacao.remove(roleta)

    return selecionados

def Roleta(populacao, vt, tempo, tempo_limite):
    maximo = sum([Valor(e, vt) for e in populacao])

    # TIMER CHECK
    if (time() - tempo) >= tempo_limite:
        return choice(populacao)

    razoes = [(Valor(e, vt) / maximo, e) for e in populacao]

    # TIMER CHECK
    if (time() - tempo) >= tempo_limite:
        return choice(populacao)

    razoes.sort(key = lambda r: r[0], reverse = True)

    # TIMER CHECK
    if (time() - tempo) >= tempo_limite:
        return choice(populacao)

    roleta, soma = [], 0
    
    for individuo in razoes:
        # TIMER CHECK
        if (time() - tempo) >= tempo_limite:
            return choice(populacao)

        soma += individuo[0]
        roleta.append((soma, individuo[1]))

    probabilidade = uniform(0, 1)

    for individuo in roleta:
        # TIMER CHECK
        if (time() - tempo) >= tempo_limite:
            return choice(roleta)[1]

        if probabilidade <= individuo[0]:
            return individuo[1]

    return roleta

def Crossover(populacao, t, vt, taxa_crossover, tempo, tempo_limite):
    novatos = []

    reprodutores = [e for e in populacao if uniform(0, 1) <= taxa_crossover]

    for _ in range(len(reprodutores) // 2):
        # TIMER CHECK
        if (time() - tempo) >= tempo_limite:
            break

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

def Mutacao(populacao, t, vt, taxa_mutacao, tempo, tempo_limite):
    candidatos, mutados = [], []

    for e in populacao:
        # TIMER CHECK
        if (time() - tempo) >= tempo_limite:
            return populacao

        if uniform(0, 1) <= taxa_mutacao:
            candidatos.append(e)
        else:
            mutados.append(e)

    for candidato in candidatos:
        # TIMER CHECK
        if (time() - tempo) >= tempo_limite:
            break

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
    tamanho_populacao = 30
    iteracoes = 100
    taxa_crossover = 0.85
    taxa_mutacao = 0.3
    tempo_limite = 5.0
    
    resultado = Genetic(t, vt, tempo_limite, iteracoes, tamanho_populacao, taxa_crossover, taxa_mutacao)
    print(resultado)