from csv import DictReader
from BeamSearch import BeamSearch
from PosTreino import MelhorCombinacaoHiperparametros

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
    nome, t, vt = entrada["nome"], int(entrada["t"]), eval(entrada["vt"])
    estado, valor, tamanho, tempo = BeamSearch(t, vt, 300, m)
    
    resultados.write(f"{nome};{m};{tempo};{estado};{valor};{tamanho}\n")