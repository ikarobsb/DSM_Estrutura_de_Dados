# Formas geométricas representadas na forma de dicionário para

forma1 = {
    'base': 7.5,
    'altura': 12,
    'tipo': 'R' # Retângulo
}

forma2 = {
    'base': 6,
    'altura': 2.5,
    'tipo': 'T' # triângulo
}

forma3 = {
    'base': 5,
    'altura': 3,
    'tipo': 'E' #Elipse
}

forma4 = {
    'base': 10,
    'altura': 5,
    'tipo': 'R' # Tipo não conhecido
}

# Forma geométrica completamente anômala
forma5 = {
    'legume': 'batata',
    'fruta': 'jabuticaba',
    'tipo': 'T' # Triângulo
}

# Inserindo as formas em uma lista para percorrer com for

lista_formas = [forma1, forma2, forma3, forma4, forma5]

# Função que calcula a área de ua forma de acordo com a base, a altura e o tipo de
from math import pi

def calcular_area(forma):
    if forma['tipo'] == 'R':    # Retângulo
        return forma['base'] * forma['altura']
    if forma['tipo'] == 'T':
        return forma['base'] * forma['altura'] / 2
    elif forma['tipo'] == 'E':
        return (forma['base'] / 2) * (forma['altura'] / 2) * pi  
    else: # Forma desconhecida
        # Gera um erro
        raise Exception('Error: Forma desconhecida')

#  Calculando a área das formas da lista:

for i in range(0, len(lista_formas)):
    print('-' * 30)
    print(f'Calculando área da forma {i + 1}')
    print(f'Tipo: {lista_formas[i]["tipo"]}; Base: {lista_formas[i]["base"]}; Altura: {lista_formas[i]["altura"]}; ÁREA: {calcular_area(lista_formas[i])}')