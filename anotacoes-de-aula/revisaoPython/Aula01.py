# LISTAS EM PYTON
# VÁRIOS VALORES EM UMA ÚNICA VARIÁVEL
valores = ['batata', 'cenoura', 1, 3, 12, True, 3, 4, 6, 9, 10, "banana"] # pode-se colocar itens de diferentes tipos



# Operações sobre listas

# 1) Percurso: percorre a lista do primeiro ao último elemento, fazendo algo com cada um deles. No caso vamos exibir cada um dos elementos da lista com um print*() --> for + "variável" (com qualquer nome) in "lista".

for v in valores:
    print(v)

# 2) Inserindo um novo elemento no final da lista: append()

valores.append("cebola")
valores.append("29")

print('Após a inserção se 2 valores no fim', valores)

# 3) Inserindo um elemento especificando a posição - Tem dois parâmetros:
#   1) Posição para inserir;
#   2) Valor a ser inserido.

valores.insert(3, 2) # inserindo 2 na posição 3
valores.insert(4, 'chuchu') # inserindo 7 na posição 4

print(valores)

# 4) Determinando a quantidade de elementos da lista

print('Número de elementos da lista', len(valores))

# 5) Renovando o último elemento da lista: pop()
ultimo = valores.pop()
print(f'{ultimo} era o último elemento da lista')
print('Após remoção do último elemento.', valores)

# 6) Removendo por posição: del()

del valores[7] # remove o elemento da posição 7
print('Após a remoção da posição 7: ', valores)

del valores[0] # remove o elemento da posição 0
print('Após a remoção da posição 0: ', valores)

# 7) Removendo por valor: remove()

valores.remove(12) # Remove o valor 29

print('Lista sem o 12', valores)

valores.remove('cebola') # Remove o valor cebola

print('Lista sem cebola', valores)

# 8) Fatiando uma lista
sublista1 = valores[0:7]
sublista2 = valores[4:10] 
print('Lista fatiada desde a posição zero até a posição 7 - 1: ', sublista1) 
print('Lista fatiada desde a posição 4 até a posição 9 - 1: ', sublista2) 
print('Lista original: ', valores)
print('Indicando valoes de 5-9 da lista original', valores[5:9])

# Sublista do início até uma posição determinada ou de posição determinada até o final:
print('Lista original de 0 até 8', valores[:8])
print('Lista original de 2 até final', valores[2:])