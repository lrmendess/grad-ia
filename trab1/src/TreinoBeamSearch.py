from csv import DictReader
from BeamSearch import BeamSearch

parametros_m = [10, 25, 50, 100]

treino_csv = open("problemas/treino.csv")
hiperparametros = list(DictReader(treino_csv, delimiter=";"))

resultados = open("resultados/beamsearch.csv", "w")
resultados.write("nome;m;tempo;estado;valor;tamanho\n")

for m in parametros_m:
    for hp in hiperparametros:
        nome, t, vt = hp["nome"], int(hp["t"]), eval(hp["vt"])
        estado, valor, tamanho, tempo = BeamSearch(t, vt, m)
        
        resultados.write(f"{nome};{m};{tempo};{estado};{valor};{tamanho}\n")
