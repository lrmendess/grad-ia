from csv import DictReader
from statistics import mean

def MaiorValor(problema_dict):
    maior = map(lambda e: e['valor'], problema_dict)
    maior = max(maior)

    return maior

with open('resultados/beamsearch.csv') as arquivo_csv:
    beam_search = list(DictReader(arquivo_csv, delimiter=';'))

    # GROUP BY PROBLEMAS
    bs_problemas = {}

    for linha in beam_search:
        nome, valor = linha['nome'], float(linha['valor'])

        chave = f"{linha['m']}"

        if nome not in bs_problemas:
            bs_problemas[nome] = list()
        
        bs_problemas[nome].append({'chave': chave, 'valor': valor})

    # NORMALIZACAO
    for k, v in bs_problemas.items():
        maior = MaiorValor(v)

        for i in range(len(v)):
            bs_problemas[k][i]['normal'] = v[i]['valor'] / maior

    # GROUP BY HIPERPARAMETROS
    bs_parametros = {}

    for linha in beam_search:
        chave = f"{linha['m']}"

        resultados = list()

        for _, v in bs_problemas.items():
            filtro = filter(lambda e: e['chave'] == chave, v)
            mapeamento = map(lambda e: e['normal'], filtro)
            resultados.extend(mapeamento)

        if chave not in bs_parametros:
            bs_parametros[chave] = resultados

    # MEDIAS DAS NORMALIZACOES
    bs_medias = {}
    
    for k, v in bs_parametros.items():
        bs_medias[k] = mean(v)

    # MELHOR HIPERPARAMETRO
    melhor_combinacao = max(bs_medias.items(), key=lambda e: e[1])

    m = melhor_combinacao[0]

    print(m)

simulated_annealing_file = open('resultados/simulatedannealing.csv')
genetic_file = open('resultados/genetic.csv')
grasp_file = open('resultados/grasp.csv')

simulated_annealing = list(DictReader(simulated_annealing_file, ';'))
genetic = list(DictReader(genetic_file, ';'))
grasp = list(DictReader(grasp_file, ';'))