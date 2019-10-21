from csv import DictReader
from SimulatedAnnealing import SimulatedAnnealing

parametros_to = [500, 100, 50]
parametros_alpha = [0.95, 0.85, 0.7]
parametros_iteracoes = [350, 500]

treino_csv = open("problemas/treino.csv")
entradas = list(DictReader(treino_csv, delimiter=";"))

resultados = open("resultados/simulatedannealing.csv", "w")
resultados.write("nome;to;alpha;iteracoes;tempo;estado;valor;tamanho\n")

for to in parametros_to:
    for alpha in parametros_alpha:
        for iteracoes in parametros_iteracoes:
            for entrada in entradas:
                nome, t, vt = entrada["nome"], int(entrada["t"]), eval(entrada["vt"])
                estado, valor, tamanho, tempo = SimulatedAnnealing(t, vt, 120, iteracoes, to, alpha)

                resultados.write(f"{nome};{to};{alpha};{iteracoes};{tempo};{estado};{valor};{tamanho}\n")