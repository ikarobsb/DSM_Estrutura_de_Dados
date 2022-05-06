from lib.deque import Deque

deque = Deque()

# Inserção de elementos na fila - prioridade normal
deque.insert_back('Mariovaldo')
deque.insert_back('Belarmina')
deque.insert_back('Valdisney')
deque.insert_back('Cristiano')
deque.insert_back('Ronaldo')
deque.insert_back('Neymar')

# Imprime os elementos da fila
print(deque)

# Inserção de elementos na fila - prioridade alta
deque.insert_front('Messi')

# Imprime os elementos do deque
print(deque)

# Remoção no final
desistente = deque.remoove_back()
print(f'Desistente: {desistente}')

# Imprime os elementos do deque
print(deque)

# Outra inserção prioritária
deque.insert_front('Bruno')

# Imprime os elementos do deque
print(deque)

# Remoção no inicio
atendido = deque.remoove_front()
print(f'Atendido: {atendido}')

# Imprime os elementos do deque
print(deque)

# Consulta do primeiro elemento
proximo = deque.peek_front()
print(f'Próximo: {proximo}')

# Imprime os elementos do deque
print(deque)

# Consulta do último elemento do deque
ultimo = deque.peek_back()
print(f'Último: {ultimo}')

# Imprime os elementos do deque
print(deque)


