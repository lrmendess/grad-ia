from csv import DictReader
from Grasp import Grasp

parametros_iteracoes = [50, 100, 200, 350, 500]
parametros_m = [2, 5, 10, 15]

treino_csv = open("problemas/treino.csv")
entradas = list(DictReader(treino_csv, delimiter=";"))

resultados = open("resultados/grasp.csv", "w")
resultados.write("nome;iteracoes;m;tempo;estado;valor;tamanho\n")

for iteracoes in parametros_iteracoes:
    for m in parametros_m:
        for entrada in entradas:
            nome, t, vt = entrada["nome"], int(entrada["t"]), eval(entrada["vt"])
            estado, valor, tamanho, tempo = Grasp(t, vt, 120, iteracoes, m)

            resultados.write(f"{nome};{iteracoes};{m};{tempo};{estado};{valor};{tamanho}\n")