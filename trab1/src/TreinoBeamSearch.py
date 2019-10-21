from csv import DictReader
from BeamSearch import BeamSearch

parametros_m = [10, 25, 50, 100]

treino_csv = open("problemas/treino.csv")
entradas = list(DictReader(treino_csv, delimiter=";"))

resultados = open("resultados/beamsearch.csv", "w")
resultados.write("nome;m;tempo;estado;valor;tamanho\n")

for m in parametros_m:
    for entrada in entradas:
        nome, t, vt = entrada["nome"], int(entrada["t"]), eval(entrada["vt"])
        estado, valor, tamanho, tempo = BeamSearch(t, vt, 120, m)
        
        resultados.write(f"{nome};{m};{tempo};{estado};{valor};{tamanho}\n")
