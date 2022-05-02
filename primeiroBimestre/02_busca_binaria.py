# ALGORITMO DE BUSCA BINÁRIA

# Dada uma lista, que deve estar PREVIAMENTE ORDENADA, e um valor de busca, divide a lista em duas metades e procura pelo valor de busca apenas na metade onde o valor poderia estar. Novas subdivisões são feitas até que se encontre o valor de busca ou que reste apenas uma sublista vazia, quando se conclui que o valor de busca não existe na lista.

from data.primos import primos #importando a lista de primos
from data.lista_nomes import nomes

#Contador de comparações
comps = 0

def busca_binaria(lista, val):

    #"global" indica que estamos usando uma variável que foi declarada fora da função
    global comps
    comps = 0

    ini = 0                 # Posição inicial da lista
    fim = len(lista) - 1    # Posição final da lista

    while ini <= fim:
        meio = (ini + fim) // 2      # Meio da lista

        # 1º caso: o valor na posição do meio da lista corresponde ao valor buscado; ENCONTRAMOS e retornamos a posição encontrada (meio)
        if val == lista[meio]:
            comps += 1
            return meio

        # 2º caso: o valor de busca é MAIOR que o valor no meio da lista
        elif val > lista[meio]:
            comps += 2
            ini = meio + 1

        # 3º o valor de busca é MENOR que o valor no meio da lista
        else:
            comps += 2
            fim = meio - 1
    # val não existe em lista
    return -1

print('\n')
print('-------------BUSCA DE NÚMEROS PRIMOS-------------\n')
print(f'1487 na lista de primos: posição {busca_binaria(primos, 1487)} comparações -> {comps}')
print(f'8008 na lista de primos: posição {busca_binaria(primos, 8008)} comparações -> {comps}')
print('\n')
print('=-' * 30)
print('\n')
print('-------------BUSCA DE NOMES-------------\n')
print(f'IKARO está na posição: {busca_binaria(nomes, "IKARO")} comparações -> {comps}')
print(f'Orkutilson está na posição: {busca_binaria(nomes, "ORKUTILSON")} comparações -> {comps}')
print(f'AARAO está na posição: {busca_binaria(nomes, "AARAO")} comparações -> {comps}')