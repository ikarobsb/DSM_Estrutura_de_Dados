from lib.binary_search_tree import BinarySearchTree

arvore = BinarySearchTree()

arvore.insert(37)
arvore.insert(20)
arvore.insert(51)
arvore.insert(3)
arvore.insert(43)
arvore.insert(0)
arvore.insert(72)
arvore.insert(11)
arvore.insert(40)
arvore.insert(8)
arvore.insert(66)
arvore.insert(19)
arvore.insert(75)
arvore.insert(82)

print('Em-ordem:')
arvore.in_order_traversal()
print('-----------------------------------------------------------')

print('Pré-ordem:')
arvore.pre_order_traversal()
print('-----------------------------------------------------------')

print('Pós-ordem:')
arvore.post_order_traversal()
print('-----------------------------------------------------------')

# Teste de existência de valores na árvore
print('Existe o valor 37?', arvore.exists(37))
print('Existe o valor 42?', arvore.exists(42))
print('Existe o valor 0?', arvore.exists(0))
print('-----------------------------------------------------------')

# Teste do min node 
minimo = arvore.min_node()
print(f'O menor valor da árvore é: {minimo[0].data}; profundidade: {minimo[1]}')

# Teste do max node
maximo = arvore.max_node()
print(f'O maior valor da árvore é: {maximo[0].data}; profundidade: {maximo[1]}')