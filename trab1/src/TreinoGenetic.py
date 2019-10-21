from csv import DictReader
from Genetic import Genetic

parametros_tamanho_populacao = [10, 20, 30]
parametros_taxa_crossover = [0.75, 0.85, 0.95]
parametros_taxa_mutacao = [0.10, 0.20, 0.30]

treino_csv = open("problemas/treino.csv")
entradas = list(DictReader(treino_csv, delimiter=";"))

resultados = open("resultados/genetic.csv", "w")
resultados.write("nome;tamanho_populacao;taxa_crossover;taxa_mutacao;tempo;estado;valor;tamanho\n")

for tamanho_populacao in parametros_tamanho_populacao:
    for taxa_crossover in parametros_taxa_crossover:
        for taxa_mutacao in parametros_taxa_mutacao:
            for entrada in entradas:
                nome, t, vt = entrada["nome"], int(entrada["t"]), eval(entrada["vt"])
                estado, valor, tamanho, tempo = Genetic(t, vt, 120, 1000, tamanho_populacao, taxa_crossover, taxa_mutacao)

                resultados.write(f"{nome};{tamanho_populacao};{taxa_crossover};{taxa_mutacao};{tempo};{estado};{valor};{tamanho}\n")