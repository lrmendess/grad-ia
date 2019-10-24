from csv import DictReader
from HillClimbing import HillClimbing

teste_csv = open("problemas/teste.csv")
entradas = list(DictReader(teste_csv, delimiter=";"))

resultados = open("resultados/teste_hillclimbing.csv", "w")
resultados.write("nome;tempo;estado;valor;tamanho\n")

for entrada in entradas:
    nome, t, vt = entrada["nome"], int(entrada["t"]), eval(entrada["vt"])
    estado, valor, tamanho, tempo = HillClimbing(t, vt, 300)

    resultados.write(f"{nome};{tempo};{estado};{valor};{tamanho}\n")