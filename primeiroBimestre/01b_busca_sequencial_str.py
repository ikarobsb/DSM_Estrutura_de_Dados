from data.lista_nomes import nomes 
from time import time

def busca_sequencial(lista, val):
    for pos in range (len(lista)):
        # Se encontra coincidência, retoena a posição
        if lista[pos] == val: return pos
    return -1 # Nada encontrado

hora_ini = time()
print(f"Orkutilson na lista {busca_sequencial(nomes, 'ORKUTILSON')}") #QDO FOR DECLARAR STRING DENTRO DE UMA FSTRING SE COMELOU COM "" COLOQUE A STR EM '' OU VISE E VERSA
hora_fim = time()
print(f'{(hora_fim - hora_ini) * 1000} ms')

hora_ini = time()
print(f"Ikaro na lista {busca_sequencial(nomes, 'IKARO')}")
hora_fim = time()
print(f'{(hora_fim - hora_ini) * 1000} ms')

hora_ini = time()
print(f"FAUSTO na lista {busca_sequencial(nomes, 'FAUSTO')}")
hora_fim = time()
print(f'{(hora_fim - hora_ini) * 1000} ms')