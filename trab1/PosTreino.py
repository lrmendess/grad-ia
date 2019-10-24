import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from csv import DictReader
from statistics import mean

def HiperResultados(nome_arquivo, hiperparametros):
    with open(nome_arquivo) as arquivo_csv:
        resultados_teste = list(DictReader(arquivo_csv, delimiter=';'))

    # GROUP BY PROBLEMAS
    problemas = {}

    for linha in resultados_teste:
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

    for linha in resultados_teste:
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

    # MELHOR HIPERPARAMETRO
    melhor_combinacao = max(medias.items(), key=lambda e: e[1])

    return melhor_combinacao[0]

if __name__ == '__main__':
    algoritmos = {
        'BS': HiperResultados('resultados/treino_beamsearch.csv', ['m']),
        'SA': HiperResultados('resultados/treino_simulatedannealing.csv', ['to', 'alpha', 'iteracoes']),
        'GE': HiperResultados('resultados/treino_genetic.csv', ['tamanho_populacao', 'taxa_crossover', 'taxa_mutacao']),
        'GR': HiperResultados('resultados/treino_grasp.csv', ['iteracoes', 'm'])
    }

    algoritmo = algoritmos[sys.argv[1]]

    ordenado = list(MediasHiperparametros(algoritmo).items())
    ordenado.sort(key=lambda e: e[1], reverse=True)
    ordenado = ordenado[:10]

    frame_normalizado = pd.DataFrame()
    frame_tempo = pd.DataFrame()

    for each in ordenado:
        k = each[0]
        frame_normalizado[k] = list(map(lambda e: e[0], algoritmo[k]))
        frame_tempo[k] = list(map(lambda e: e[1], algoritmo[k]))

    sns.boxplot(data=frame_normalizado)
    plt.show()

    sns.boxplot(data=frame_tempo)
    plt.show()