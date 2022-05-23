from lib.doubly_linked_list import DoublyLinkedList

lista = DoublyLinkedList()
print(lista)

# Inserção em lista vazia; a posição será ignorada
lista.insert(5, 'Epaminondas')
print(lista)

# Inserção no início da lista
lista.insert_head('Filisberto') # Equivale a: lista.insert(0, 'Filisberto')
print(lista)

# Inserção no final da lista
lista.insert_tail('Jeruza')     # Equivale a: lista.insert(lista.count, 'Jeruza')
print(lista)

# Inserção em posição intermediária
lista.insert(2, 'Laudicéia')
print(lista)
lista.insert(1, 'Drusila')
print(lista)

# Inserção de um item duplicado
lista.insert_tail('Epaminondas')
print(lista)

# Inserção de um item extra na posição 3
lista.insert(3, 'Praxedes')
print(lista)

# Teste de consulta em difentes posições
val_primeiro = lista.peek_head()
val_ultimo = lista.peek_tail()
val_3 = lista.peek(3)
val_1 = lista.peek(1)
print(f'Primeiro: {val_primeiro}, último: {val_ultimo}, pos. 1: {val_1}, pos. 3: {val_3}')

# Teste de busca por valor
pos_jeruza = lista.index('Jeruza')
pos_epaminondas = lista.index('Epaminondas')
pos_laudiceia = lista.index('Laudicéia')
pos_aristides = lista.index('Aristides')
print(f'POSIÇÕES -> Jeruza: {pos_jeruza}, Epaminondas: {pos_epaminondas}, Laudicéia: {pos_laudiceia}, Aristides: {pos_aristides}')

# Encontrando a posição do segundo Epaminondas, buscando a partir
# da posição seguinte à do primeiro Epaminondas
pos_epaminondas2 = lista.index('Epaminondas', pos_epaminondas + 1)
print(f'Posição do segundo Epaminondas: {pos_epaminondas2}')

# Exclusão do primeiro elemento
excl_primeiro = lista.remove_head()
print(f'Excluído na primeira posição: {excl_primeiro}')
print(lista)

# Exclusão do último elemento
excl_ultimo = lista.remove_tail()
print(f'Excluído da última posição: {excl_ultimo}')
print(lista)

# Exclusão do nodo da posição 3
excl_3 = lista.remove(3)
print(f'Excluído da posição 3: {excl_3}')
print(lista)

# Exclusão do nodo da posição 1
excl_1 = lista.remove(1)
print(f'Excluído da posição 3: {excl_1}')
print(lista)