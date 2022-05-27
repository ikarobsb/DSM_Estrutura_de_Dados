from lib.graph import Graph

familia = Graph(True)   # Grafo será direcionado
print(familia)

familia.add_vertex('Ariovaldo')
familia.add_vertex('Clementina')
familia.add_vertex('Aristeu')
familia.add_vertex('Clementina') # Tentativa de inserção repetida
familia.add_vertex('Gercina')

print(familia)

familia.add_edge('Ariovaldo', 'Clementina', 'casado com')
familia.add_edge('Ariovaldo', 'Aristeu', 'pai')
familia.add_edge('Clementina', 'Ariovaldo', 'casada com')
familia.add_edge('Clementina', 'Cleusa', 'mãe')
familia.add_edge('Cleusa', 'Clementina', 'filha')

print('-----------------------')
print(familia)

# Não direcionado, equivale a cidades = Graph(false)
cidades = Graph()

cidades.add_edge('Franca', 'Claraval')
cidades.add_edge('Franca', 'Cristais Paulista', 'Rod. Candido Portinari')

print('-----------------------')
print(cidades)


print('-----------------------')
print(familia)

# Remoções de vértice
familia.remove_vertex('Gercina')
print('(Removido Gercina)', familia)
familia.remove_vertex('Segismundo')     # Não existe no grafo, deve ser ignorado
print('(Removido Segismundo)', familia)
# familia.remove_vertex('Aristeu') # Nodo é referenciado por outro; não remove
# familia.remove_vertex('Ariovaldo') # Nodo tem grau > 0; não remove

print('#########################')
print(familia, "\n\n", cidades)     # Quebra duas linhas

familia.remove_edge('Ariovaldo', 'Clementina', 'casado com')
cidades.remove_edge('Cristais Paulista', 'Franca', 'Rod. Candido Portinari')

print("\n\n", familia, "\n\n", cidades)     # Quebra duas linhas