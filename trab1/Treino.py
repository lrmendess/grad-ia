import sys

from csv import DictReader
from BeamSearch import BeamSearch
from SimulatedAnnealing import SimulatedAnnealing
from Genetic import Genetic
from Grasp import Grasp

run_all = len(sys.argv) <= 1
algoritmo = 'ALL' if run_all else sys.argv[1]

if algoritmo == 'BS' or run_all:
    parametros_m = [10, 25, 50, 100]

    treino_csv = open("problemas/treino.csv")
    entradas = list(DictReader(treino_csv, delimiter=";"))

    resultados = open("resultados/treino_beamsearch.csv", "w")
    resultados.write("nome;m;tempo;estado;valor;tamanho\n")

    for m in parametros_m:
        for entrada in entradas:
            nome, t, vt = entrada["nome"], float(entrada["t"]), eval(entrada["vt"])
            estado, valor, tamanho, tempo = BeamSearch(t, vt, 120, m)
            
            resultados.write(f"{nome};{m};{tempo};{estado};{valor};{tamanho}\n")


if algoritmo == 'SA' or run_all:
    parametros_to = [500, 100, 50]
    parametros_alpha = [0.95, 0.85, 0.7]
    parametros_iteracoes = [350, 500]

    treino_csv = open("problemas/treino.csv")
    entradas = list(DictReader(treino_csv, delimiter=";"))

    resultados = open("resultados/treino_simulatedannealing.csv", "w")
    resultados.write("nome;to;alpha;iteracoes;tempo;estado;valor;tamanho\n")

    for to in parametros_to:
        for alpha in parametros_alpha:
            for iteracoes in parametros_iteracoes:
                for entrada in entradas:
                    nome, t, vt = entrada["nome"], float(entrada["t"]), eval(entrada["vt"])
                    estado, valor, tamanho, tempo = SimulatedAnnealing(t, vt, 120, iteracoes, to, alpha)

                    resultados.write(f"{nome};{to};{alpha};{iteracoes};{tempo};{estado};{valor};{tamanho}\n")

if algoritmo == 'GE' or run_all:
    parametros_tamanho_populacao = [10, 20, 30]
    parametros_taxa_crossover = [0.75, 0.85, 0.95]
    parametros_taxa_mutacao = [0.10, 0.20, 0.30]

    treino_csv = open("problemas/treino.csv")
    entradas = list(DictReader(treino_csv, delimiter=";"))

    resultados = open("resultados/treino_genetic.csv", "w")
    resultados.write("nome;tamanho_populacao;taxa_crossover;taxa_mutacao;tempo;estado;valor;tamanho\n")

    for tamanho_populacao in parametros_tamanho_populacao:
        for taxa_crossover in parametros_taxa_crossover:
            for taxa_mutacao in parametros_taxa_mutacao:
                for entrada in entradas:
                    nome, t, vt = entrada["nome"], float(entrada["t"]), eval(entrada["vt"])
                    estado, valor, tamanho, tempo = Genetic(t, vt, 120, 100, tamanho_populacao, taxa_crossover, taxa_mutacao)

                    resultados.write(f"{nome};{tamanho_populacao};{taxa_crossover};{taxa_mutacao};{tempo};{estado};{valor};{tamanho}\n")

if algoritmo == 'GR' or run_all:
    parametros_iteracoes = [50, 100, 200, 350, 500]
    parametros_m = [2, 5, 10, 15]

    treino_csv = open("problemas/treino.csv")
    entradas = list(DictReader(treino_csv, delimiter=";"))

    resultados = open("resultados/treino_grasp.csv", "w")
    resultados.write("nome;iteracoes;m;tempo;estado;valor;tamanho\n")

    for iteracoes in parametros_iteracoes:
        for m in parametros_m:
            for entrada in entradas:
                nome, t, vt = entrada["nome"], float(entrada["t"]), eval(entrada["vt"])
                estado, valor, tamanho, tempo = Grasp(t, vt, 120, iteracoes, m)

                resultados.write(f"{nome};{iteracoes};{m};{tempo};{estado};{valor};{tamanho}\n")