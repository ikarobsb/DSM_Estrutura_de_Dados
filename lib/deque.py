"""
    ESTRUTURA DE DADOS DEQUE

    Deque (Double-Ended Queue) é uma estrutura derivada da fila que permite inserções e remoções em qualquer uma de sias extremidades. Com isso, o deque pode se comportar como uma fila comum, como uma fila em qie são admitidos elementos prioritários e até como uma fila invertida (como se fosse uma pilha).
"""

class Deque:
    # Constructor
    def __init__(self):
        self.__data = [] # LIsta vazia

    """
    Método para imprimir os elementos da fila
    Esse é um método especial do Python, que é chamado automaticamente quando se tenta imprimir uma instância da classe.
    """
    def __str__(self):
        return str(self.__data)
    
    """Método para verificar se a fila está vazia"""
    @property
    def is_empty(self):
        return len(self.__data) == 0

    """Método para incluir um elemento no inicio da fila"""
    def insert_front(self, val):
        self.__data.insert(0, val)

    """Método para incluir um elemento no final da fila"""
    def insert_back(self, val):
        self.__data.append(val)

    """Método para retirar o primeiro elemento da fila"""
    def remoove_front(self):
        if self.is_empty:
            raise Exception('ERRO: impossível remover de uma fila vazia')
        return self.__data.pop(0)
    
    """Método para retirar o último elemento da fila"""
    def remoove_back(self):
        if self.is_empty:
            raise Exception('ERRO: impossível remover de uma fila vazia')
        return self.__data.pop()
    
    """Método para consultar o valor na cabeça da fila, sem retirá-lo de lá"""
    def peek_front(self):
        if self.is_empty:
            raise Exception('ERRO: impossível consultar a cabeça de uma fila vazia')
        return self.__data[0]

    """Método para consultar o valor na cauda da fila, sem retirá-lo de lá"""
    def peek_back(self):
        if self.is_empty:
            raise Exception('ERRO: impossível consultar a cauda de uma fila vazia')
        return self.__data[-1]
    

