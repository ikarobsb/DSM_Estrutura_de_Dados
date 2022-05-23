from lib.graph import Graph

familia = Graph(True)

familia = Graph(True)   # Grafo será direcionado
print(familia)

familia.add_vertex('Ariovaldo')
familia.add_vertex('Clementina')
familia.add_vertex('Aristeu')
familia.add_vertex('Clementina') # Tentativa de inserção repetida

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