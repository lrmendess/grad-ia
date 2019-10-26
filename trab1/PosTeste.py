import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from csv import DictReader
from statistics import mean, stdev

def Problemas(nome_arquivo):
    problemas = open(nome_arquivo)
    problemas = DictReader(problemas, delimiter=';')
    problemas = map(lambda e: e['nome'], problemas)
    problemas = list(problemas)

    return problemas

def MakeFrame(nome_arquivo):
    problemas = Problemas('problemas/teste.csv')

    frame = pd.DataFrame(index=problemas)

    algoritmo = open(nome_arquivo)
    algoritmo = list(DictReader(algoritmo, delimiter=';'))

    valores = list(map(lambda e: float(e['valor']), algoritmo))
    tempos  = list(map(lambda e: float(e['tempo']), algoritmo))

    frame['valor'] = valores
    frame['tempo'] = tempos

    return frame

def Media(frame, coluna):
    lista = frame[coluna].tolist()
    return mean(lista)

def DP(frame, coluna):
    lista = frame[coluna].tolist()
    return stdev(lista)

hc = MakeFrame('resultados/teste_hillclimbing.csv')
bs = MakeFrame('resultados/teste_beamsearch.csv')
sa = MakeFrame('resultados/teste_simulatedannealing.csv')
ge = MakeFrame('resultados/teste_genetic.csv')
gr = MakeFrame('resultados/teste_grasp.csv')

p_valores = list(zip(
    hc['valor'].tolist(),
    bs['valor'].tolist(),
    sa['valor'].tolist(),
    ge['valor'].tolist(),
    gr['valor'].tolist()))

p_maiores_valores = map(lambda e: max(e), p_valores)

# CADA PROBLEMA NORMALIZADO
p_normalizados = zip(p_maiores_valores, p_valores)
p_normalizados = list(map(lambda e: [v / e[0] for v in e[1]], p_normalizados))

# TRANSPOSICAO PARA ENCAIXAR NO DATAFRAME DO PANDAS
p_transpostos = list(map(list, zip(*p_normalizados)))

hc['normalizado'] = p_transpostos[0]
bs['normalizado'] = p_transpostos[1]
sa['normalizado'] = p_transpostos[2]
ge['normalizado'] = p_transpostos[3]
gr['normalizado'] = p_transpostos[4]

# MEDIA E DESVIO PADRAO DOS VALORES DAS METAHEURISTICAS
frame_valores = pd.DataFrame(index=['hs', 'bs', 'sa', 'ge', 'gr'])

frame_valores['media'] = [
    Media(hc, 'valor'),
    Media(bs, 'valor'),
    Media(sa, 'valor'),
    Media(ge, 'valor'),
    Media(gr, 'valor')]

frame_valores['dp'] = [
    DP(hc, 'valor'),
    DP(bs, 'valor'),
    DP(sa, 'valor'),
    DP(ge, 'valor'),
    DP(gr, 'valor')]

print('======= VALORES =======')
print(frame_valores, end='\n\n')

# MEDIA E DESVIO PADRAO DOS TEMPOS DAS METAHEURISTICAS
frame_tempos = pd.DataFrame(index=['hs', 'bs', 'sa', 'ge', 'gr'])

frame_tempos['media'] = [
    Media(hc, 'tempo'),
    Media(bs, 'tempo'),
    Media(sa, 'tempo'),
    Media(ge, 'tempo'),
    Media(gr, 'tempo')]

frame_tempos['dp'] = [
    DP(hc, 'tempo'),
    DP(bs, 'tempo'),
    DP(sa, 'tempo'),
    DP(ge, 'tempo'),
    DP(gr, 'tempo')]

print('======= TEMPOS =======')
print(frame_tempos, end='\n\n')

frame_normalizados = pd.DataFrame(index=['hs', 'bs', 'sa', 'ge', 'gr'])

frame_normalizados['media'] = [
    Media(hc, 'normalizado'),
    Media(bs, 'normalizado'),
    Media(sa, 'normalizado'),
    Media(ge, 'normalizado'),
    Media(gr, 'normalizado')]

frame_normalizados['dp'] = [
    DP(hc, 'normalizado'),
    DP(bs, 'normalizado'),
    DP(sa, 'normalizado'),
    DP(ge, 'normalizado'),
    DP(gr, 'normalizado')]

print('======= NORMALIZADOS =======')
print(frame_normalizados, end='\n\n')

# RANKING POR RESULTADO ABSOLUTO
problemas = Problemas('problemas/teste.csv')

lista_ranking_absoluto = [list(zip(['hc', 'bs', 'sa', 'ge', 'gr'], pv)) for pv in p_valores]
lista_ranking_absoluto = [sorted(r, key=lambda e: e[1], reverse=True) for r in lista_ranking_absoluto]

ranking_absoluto = {'hc': 0, 'bs': 0, 'sa': 0, 'ge': 0, 'gr': 0}

for each in lista_ranking_absoluto:
    posicoes = list(map(lambda e: e[0], each))
    ranking_absoluto['hc'] += posicoes.index('hc') + 1
    ranking_absoluto['bs'] += posicoes.index('bs') + 1
    ranking_absoluto['sa'] += posicoes.index('sa') + 1
    ranking_absoluto['ge'] += posicoes.index('ge') + 1
    ranking_absoluto['gr'] += posicoes.index('gr') + 1

ranking_absoluto['hc'] /= len(lista_ranking_absoluto)
ranking_absoluto['bs'] /= len(lista_ranking_absoluto)
ranking_absoluto['sa'] /= len(lista_ranking_absoluto)
ranking_absoluto['ge'] /= len(lista_ranking_absoluto)
ranking_absoluto['gr'] /= len(lista_ranking_absoluto)

print("====== RANKING ABSOLUTO ======")
print(list(sorted(ranking_absoluto.items(), key=lambda e: e[1])), end='\n\n')

# RANKING POR RESULTADO NORMALIZADO
print("====== RANKING NORMALIZADO ======")
ranking_normalizado = frame_normalizados['media'].tolist()
ranking_normalizado = list(zip(['hc', 'bs', 'sa', 'ge', 'gr'], ranking_normalizado))
ranking_normalizado.sort(key=lambda e: e[1], reverse=True)
print(ranking_normalizado)

# BOXPLOTS VALORES NORMALIZADOS
box_normalizados = pd.DataFrame()

box_normalizados['hc'] = hc['normalizado'].tolist()
box_normalizados['bs'] = bs['normalizado'].tolist()
box_normalizados['sa'] = sa['normalizado'].tolist()
box_normalizados['ge'] = ge['normalizado'].tolist()
box_normalizados['gr'] = gr['normalizado'].tolist()

sns.boxplot(data=box_normalizados)
plt.show()

# BOXPLOTS TEMPOS
box_tempos = pd.DataFrame()

box_tempos['hc'] = hc['tempo'].tolist()
box_tempos['bs'] = bs['tempo'].tolist()
box_tempos['sa'] = sa['tempo'].tolist()
box_tempos['ge'] = ge['tempo'].tolist()
box_tempos['gr'] = gr['tempo'].tolist()

sns.boxplot(data=box_tempos)
plt.show()
