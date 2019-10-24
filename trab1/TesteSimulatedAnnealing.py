from csv import DictReader
from SimulatedAnnealing import SimulatedAnnealing
from PosTreino import MelhorCombinacaoHiperparametros

parametros = MelhorCombinacaoHiperparametros(
    'resultados/treino_simulatedannealing.csv',
    ['to', 'alpha', 'iteracoes']
)

parametros = parametros.split(';')

treino_csv = open("problemas/teste.csv")
entradas = list(DictReader(treino_csv, delimiter=";"))

resultados = open("resultados/teste_simulatedannealing.csv", "w")
resultados.write("nome;to;alpha;iteracoes;tempo;estado;valor;tamanho\n")

to, alpha, iteracoes = float(parametros[0]), float(parametros[1]), int(parametros[2])

for entrada in entradas:
    nome, t, vt = entrada["nome"], int(entrada["t"]), eval(entrada["vt"])
    estado, valor, tamanho, tempo = SimulatedAnnealing(t, vt, 300, iteracoes, to, alpha)

    resultados.write(f"{nome};{to};{alpha};{iteracoes};{tempo};{estado};{valor};{tamanho}\n")