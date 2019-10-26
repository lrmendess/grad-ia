import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from csv import DictReader
from statistics import mean

def HiperResultados(nome_arquivo, hiperparametros):
    with open(nome_arquivo) as arquivo_csv:
        resultados_treino = list(DictReader(arquivo_csv, delimiter=';'))

    # GROUP BY PROBLEMAS
    problemas = {}

    for linha in resultados_treino:
        nome, valor, tempo = linha['nome'], float(linha['valor']), float(linha['tempo'])
        
        chave = [linha[p] for p in hiperparametros]
        chave = ';'.join(chave)

        if nome not in problemas:
            problemas[nome] = list()
        
        problemas[nome].append({'chave': chave, 'valor': valor, 'tempo': tempo})
    

    # NORMALIZACAO
    for k, v in problemas.items():
        maior = map(lambda e: e['valor'], v)
        maior = max(maior)

        for i in range(len(v)):
            problemas[k][i]['normal'] = v[i]['valor'] / maior

    # GROUP BY HIPERPARAMETROS
    parametros = {}

    for linha in resultados_treino:
        chave = [linha[p] for p in hiperparametros]
        chave = ';'.join(chave)

        resultados = list()

        for _, v in problemas.items():
            filtro = filter(lambda e: e['chave'] == chave, v)
            mapeamento = map(lambda e: (e['normal'], e['tempo']), filtro)
            resultados.extend(mapeamento)

        if chave not in parametros:
            parametros[chave] = resultados

    return parametros

# MEDIAS DAS NORMALIZACOES
def MediasHiperparametros(parametros):
    medias = {}
    
    for k, v in parametros.items():
        normalizados = map(lambda e: e[0], v)
        medias[k] = mean(normalizados)

    return medias

def MelhorCombinacaoHiperparametros(arquivo, parametros):
    resultados = HiperResultados(arquivo, parametros)
    medias = MediasHiperparametros(resultados)

    melhor_combinacao = max(medias.items(), key=lambda e: e[1])

    return melhor_combinacao[0]

if __name__ == '__main__':
    parametros = {
        'BS': ['m'],
        'SA': ['to', 'alpha', 'iteracoes'],
        'GE': ['tamanho_populacao', 'taxa_crossover', 'taxa_mutacao'],
        'GR': ['iteracoes', 'm']
    }

    algoritmos = {
        'BS': HiperResultados('resultados/treino_beamsearch.csv', parametros['BS']),
        'SA': HiperResultados('resultados/treino_simulatedannealing.csv', parametros['SA']),
        'GE': HiperResultados('resultados/treino_genetic.csv', parametros['GE']),
        'GR': HiperResultados('resultados/treino_grasp.csv', parametros['GR'])
    }

    algoritmo = algoritmos[sys.argv[1]]

    medias_hiperparametros = MediasHiperparametros(algoritmo)
    
    ordenado = list(medias_hiperparametros.items())
    ordenado.sort(key=lambda e: e[1], reverse=True)
    ordenado = ordenado[:10]

    frame_normalizado = pd.DataFrame()
    frame_tempo = pd.DataFrame()

    for each in ordenado:
        k = each[0]
        frame_normalizado[k] = list(map(lambda e: e[0], algoritmo[k]))
        frame_tempo[k] = list(map(lambda e: e[1], algoritmo[k]))

    melhor_combinacao = max(medias_hiperparametros.items(), key=lambda e: e[1])
    melhor_combinacao = zip(parametros[sys.argv[1]], melhor_combinacao[0].split(';'))
    melhor_combinacao = list(melhor_combinacao)
    melhor_combinacao = map(lambda e: f"{e[0]}={e[1]}", melhor_combinacao)

    print('Melhor combinação de hiperparametros:')
    print(', '.join(melhor_combinacao))

    sns.boxplot(data=frame_normalizado)
    plt.show()

    sns.boxplot(data=frame_tempo)
    plt.show()