from data.primos import primos #importa o arquivo primos.py da pasta data
from time import time #importa a biblioteca tima

def busca_sequencial(val, lista):
    for pos in range (len(lista)):
        # Se encontra coincidência, retoRna a posição
        if lista[pos] == val: return pos
    return -1 # Nada encontrado

# Buscando números primos
hora_ini = time()
print(f'Poisção do 1487: {busca_sequencial(1487, primos)}')
hora_fim = time()
print(f'Tempo gasto {(hora_fim - hora_ini)}')

hora_ini = time()
print(f'Poisção do 7603: {busca_sequencial(7603, primos)}')
hora_fim = time()
print(f'Tempo gasto {(hora_fim - hora_ini)}')

hora_ini = time()
print(f'Poisção do 8008: {busca_sequencial(8008, primos)}')
hora_fim = time()
print(f'Tempo gasto {(hora_fim - hora_ini)}')
#como o Python cria uma pasta cache e armazena os dados de forma binária, por isso, uma segunda busca é muito mais eficiente.


