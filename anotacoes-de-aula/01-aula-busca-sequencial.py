################################################################################
#  Busca sequenial 
# Procura por um valor na lista, partindo do primeiro elemento até o último. Retorna a posição do elemento, caso ele exista, ou -1 se o elemento não existir.
nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 47, 51, 53, 57, 60]

"""
    Função que implementa a busca sequencial
    Procura por valores dentro da lista
"""

def busca_sequencial(val, lista):
    for pos in range (len(lista)):
        # Se encontra coincidência, retoena a posição
        if lista[pos] == val: return pos
    return -1 # Nada encontrado

# TESTE

print(f'Posição de 27: {busca_sequencial(27, nums)}')
print(f'Posição de 40: {busca_sequencial(48, nums)}') # Deverá retornar -1



