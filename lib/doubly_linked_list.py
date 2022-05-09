"""
    Classe que representa uma unidade de informação na lista duplamente encadeada
"""

class Node:
    # Método construtor
    def __init__(self):
        self.data = None # Dado do usuário
        self.next = None # Ponteiro para o próximo nó
        self.prev = None # Ponteiro para nó anterior

######################################################################################

"""
    Estrutura de dados LISTA DUPLAMENTE ENCADEADA
    Trata-se de uma lista linear, em que seus elementos (nodos) não estão adjacentes fisicamente uns aos outros, mas ligados logicamente por meio de poneiros que indicam o anterior e o próximo nodo da sequência. Não tem restrição de acesso - inserções, exclusões e consultas podem ser realizadas em qualquer posição da lista.
"""

class DoublyLinkedList:
    # Método construtor
    def __init__(self):
        self.__head = None # Aponta para o primeiro nodo da lista
        self.__tail = None # Aponta para o último elemento da lista
        self.__size = 0 # Tamanho da lista


