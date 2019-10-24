import sys

from csv import DictReader
from HillClimbing import HillClimbing
from BeamSearch import BeamSearch
from SimulatedAnnealing import SimulatedAnnealing
from Genetic import Genetic
from Grasp import Grasp
from PosTreino import MelhorCombinacaoHiperparametros

run_all = len(sys.argv) <= 1
algoritmo = 'ALL' if run_all else sys.argv[1]

if algoritmo == 'HC' or run_all:
    teste_csv = open("problemas/teste.csv")
    entradas = list(DictReader(teste_csv, delimiter=";"))

    resultados = open("resultados/teste_hillclimbing.csv", "w")
    resultados.write("nome;tempo;estado;valor;tamanho\n")

    for entrada in entradas:
        nome, t, vt = entrada["nome"], float(entrada["t"]), eval(entrada["vt"])
        estado, valor, tamanho, tempo = HillClimbing(t, vt, 300)

        resultados.write(f"{nome};{tempo};{estado};{valor};{tamanho}\n")

if algoritmo == 'BS' or run_all:
    parametros = MelhorCombinacaoHiperparametros(
        'resultados/treino_beamsearch.csv',
        ['m']
    )

    parametros = parametros.split(';')

    m = int(parametros[0])

    teste_csv = open("problemas/teste.csv")
    entradas = list(DictReader(teste_csv, delimiter=";"))

    resultados = open("resultados/teste_beamsearch.csv", "w")
    resultados.write("nome;m;tempo;estado;valor;tamanho\n")

    for entrada in entradas:
        nome, t, vt = entrada["nome"], float(entrada["t"]), eval(entrada["vt"])
        estado, valor, tamanho, tempo = BeamSearch(t, vt, 300, m)
        
        resultados.write(f"{nome};{m};{tempo};{estado};{valor};{tamanho}\n")

if algoritmo == 'SA' or run_all:
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
        nome, t, vt = entrada["nome"], float(entrada["t"]), eval(entrada["vt"])
        estado, valor, tamanho, tempo = SimulatedAnnealing(t, vt, 300, iteracoes, to, alpha)

        resultados.write(f"{nome};{to};{alpha};{iteracoes};{tempo};{estado};{valor};{tamanho}\n")

if algoritmo == 'GE' or run_all:
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
        nome, t, vt = entrada["nome"], float(entrada["t"]), eval(entrada["vt"])
        estado, valor, tamanho, tempo = Genetic(t, vt, 300, 100, tamanho_populacao, taxa_crossover, taxa_mutacao)

        resultados.write(f"{nome};{tamanho_populacao};{taxa_crossover};{taxa_mutacao};{tempo};{estado};{valor};{tamanho}\n")

if algoritmo == 'GR' or run_all:
    parametros = MelhorCombinacaoHiperparametros(
        'resultados/treino_grasp.csv',
        ['iteracoes', 'm']
    )

    parametros = parametros.split(';')

    treino_csv = open("problemas/teste.csv")
    entradas = list(DictReader(treino_csv, delimiter=";"))

    resultados = open("resultados/teste_grasp.csv", "w")
    resultados.write("nome;iteracoes;m;tempo;estado;valor;tamanho\n")

    iteracoes, m = int(parametros[0]), int(parametros[1])

    for entrada in entradas:
        nome, t, vt = entrada["nome"], float(entrada["t"]), eval(entrada["vt"])
        estado, valor, tamanho, tempo = Grasp(t, vt, 300, iteracoes, m)

        resultados.write(f"{nome};{iteracoes};{m};{tempo};{estado};{valor};{tamanho}\n")