"""
Uma fila é uma estrutura de dados dinâmica que admite remoção de elementos e inserção de novos objetos. Mais especificamente, uma fila (= queue) é uma estrutura sujeita à seguinte regra de operação: sempre que houver uma remoção, o elemento removido é o que está na estrutura há mais tempo.

Enquee --> incluir um elemento ao final da fila, semelhante ao push da fila.

Dequeue --> retirar o primeiro elemento inserido na fila.

A diferença entre pilha e fila é a saída - o primeiro a chegar é o primeiro a sair *FIFO - first in, first out*

Trata-se de uma fila por estrita ordem de chegada.

Início da fila = cabeça

FInal da fila = cauda.
"""

class Queue:
    """Método construtor"""
    def __init__(self):
        # Inicializa uma lista vazia
        self.__data = []

    """Método para incluir um elemento no final da fila"""
    def enqueue(self, val):
        self.__data.append(val)

    """Método para retirar o primeiro elemento da fila"""
    def dequeue(self):
        if self.is_empty:
            raise Exception('ERRO: impossível remover de uma fila vazia')
        # Remove o primeiro elemento da fila
        return self.__data.pop(0)
    
    """Método que consulta o valor na cabeça da fila, sem retirá-lo de lá"""
    def peek(self):
        if self.is_empty:
            raise Exception('ERRO: impossível consultar a cabeça de uma fila vazia')
        return self.__data[0]
    
    """
    Método para imprimir os elementos da fila
    Esse é um método especial do Python, que é chamado automaticamente quando se tenta imprimir uma instância da classe.
    """
    def __str__(self):
        return str(self.__data)
    
    """Método para verificar o tamanho da fila"""
    def size(self):
        return len(self.__data)

    
    """Método para verificar se a fila está vazia"""
    @property
    def is_empty(self):
        return len(self.__data) == 0





