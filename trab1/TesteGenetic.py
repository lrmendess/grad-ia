from csv import DictReader
from Genetic import Genetic
from PosTreino import MelhorCombinacaoHiperparametros

parametros = MelhorCombinacaoHiperparametros(
    'resultados/treino_genetic.csv',
    ['tamanho_populacao', 'taxa_crossover', 'taxa_mutacao']
)

parametros = parametros.split(';')

tamanho_populacao, taxa_crossover, taxa_mutacao = int(parametros[0]), float(parametros[1]), float(parametros[2])

teste_csv = open("problemas/teste.csv")
entradas = list(DictReader(teste_csv, delimiter=";"))

resultados = open("resultados/teste_genetic.csv", "w")
resultados.write("nome;tamanho_populacao;taxa_crossover;taxa_mutacao;tempo;estado;valor;tamanho\n")

for entrada in entradas:
    nome, t, vt = entrada["nome"], int(entrada["t"]), eval(entrada["vt"])
    estado, valor, tamanho, tempo = Genetic(t, vt, 300, 100, tamanho_populacao, taxa_crossover, taxa_mutacao)

    resultados.write(f"{nome};{tamanho_populacao};{taxa_crossover};{taxa_mutacao};{tempo};{estado};{valor};{tamanho}\n")