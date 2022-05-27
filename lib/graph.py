"""
    ESTRUTURA DE DADOS GRAFO
    É uma estrutura de dados não-linear, formada por vértices
    (ou nodos) e arestas. Tem como principal finalidade
    representar as relações entre os vértices, por meio das
    arestas. Tem várias aplicações, como a representação de
    redes de computadores, mapas e caminhos e redes sociais.
"""
class Graph:

    """ Método construtor """
    def __init__(self, is_directed = False):
        self.__is_directed = is_directed # O grafo é direcionado?
        self.__data = {}    # Dicionário vazio

    """
        Método que adiciona um vértice
    """
    def add_vertex(self, val):
        # Verifica se o vértice já existe no dicionário.
        # Só cria o vértice se não existir ainda.
        if not val in self.__data:
            self.__data[val] = set() # Conjunto vazio

    """
        Método que adiciona uma aresta entre dois vértices
    """
    def add_edge(self, origin, dest, rel = None):
        # Cria os vértices de origem e destino,
        # caso não existam ainda
        if not origin in self.__data: self.add_vertex(origin)
        if not dest in self.__data: self.add_vertex(dest)

        # Coloca a descrição da relação em maiúsculas,
        # se ela tiver sido passada
        if not rel is None: rel = rel.upper()

        # Monta a aresta
        edge1 = (dest, rel)  # Isto é uma tupla

        # Adiciona a relação origem->destino
        self.__data[origin].add(edge1)

        # Se o grafo não for direcionado, adiciona a relação
        # origem<-destino
        if not self.__is_directed:
            edge2 = (origin, rel)   # Tupla
            self.__data[dest].add(edge2)

    """
        Método que retorna o grau (número de arestas) 
        de um vértice
    """
    def degree(self, vertex):
        # Se vertex existir no dicionário self.__data,
        # retorna o número de elementos do conjunto de
        # arestas correspondente
        if vertex in self.__data: return len(self.__data[vertex])
        # vertex não existe, retorna None
        else: return 0

    """
        Método que verifica se um determinado vértice é referenciado
        por outro
    """
    def __is_referenced(self, vertex):
        for vtx_ref in self.__data.keys():    # Percorrendo o dicionário
            for edge in self.__data[vtx_ref]: # Percorrendo as tuplas
                # Verifica se o primeiro elemento da tupla é o vértice
                if vertex == edge[0]: return True
        return False
    
    """
        Método que remove um vértice do grafo
    """
    def remove_vertex(self, vertex):
        # Para ser removido, um vértice deve ter grau 0,
        # ou seja, não ter arestas associadas, nem ser referenciado
        # por outro vértice
        if self.degree(vertex) > 0:
            raise Exception('ERRO: não é possível remover vértice de grau > 0.')
        elif self.__is_referenced(vertex):
            raise Exception('ERRO: não é possível remover um vértice referenciado por outro.')
        # Grau 0, sem referências, remoção OK
        elif vertex in self.__data: del self.__data[vertex]

    """
        Método que remove uma aresta do grafo
    """
    def remove_edge(self, origin, dest, rel = None):
        if rel is not None: rel = rel.upper()   # Coloca rel em maiúsculas

        edge1 = (dest, rel)
        # Retira a tupla edge1 do conjunto de arestas do vértice de origem
        self.__data[origin].discard(edge1)
        
        # Se o grafo não for direcionado, precisamos remover também a aresta
        # em sentido contrário
        if not self.__is_directed:
            edge2 = (origin, rel)
            self.__data[dest].discard(edge2)
    
    """
        Método que representa o grafo como string
    """
    def __str__(self):
        output = str(self.__data)
        output += ', is_directed: ' + str(self.__is_directed)
        return output

##################################################