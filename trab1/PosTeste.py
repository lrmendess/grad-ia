import pandas as pd

from csv import DictReader
from statistics import mean, stdev

def CalculosTeste(nome_arquivo):
    algoritmo = open(nome_arquivo)
    algoritmo = list(DictReader(algoritmo, delimiter=';'))

    valores = list(map(lambda e: float(e['valor']), algoritmo))
    tempos  = list(map(lambda e: float(e['tempo']), algoritmo))

    maior_valor = max(valores)
    normalizados = [v / maior_valor for v in valores]

    frame = pd.DataFrame(index=['valores', 'normalizados'])
    frame['media'] = [mean(valores), mean(normalizados)]
    frame['dp'] = [stdev(valores), stdev(normalizados)]

    return frame, valores, tempos, normalizados

print(CalculosTeste('resultados/teste_beamsearch.csv'))