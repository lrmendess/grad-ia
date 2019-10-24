from csv import DictReader
from Grasp import Grasp
from PosTreino import MelhorCombinacaoHiperparametros

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
    nome, t, vt = entrada["nome"], int(entrada["t"]), eval(entrada["vt"])
    estado, valor, tamanho, tempo = Grasp(t, vt, 300, iteracoes, m)

    resultados.write(f"{nome};{iteracoes};{m};{tempo};{estado};{valor};{tamanho}\n")