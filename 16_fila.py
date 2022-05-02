from lib.queue import Queue

fila = Queue()

fila.enqueue('Mariovaldo')
fila.enqueue('Belarmina')
fila.enqueue('Valdisney')
fila.enqueue('Cristiano')
fila.enqueue('Ronaldo')
fila.enqueue('Messi')

# Imprime os elementos da fila
print(fila)

# Atende o primeiro da fila
atendido = fila.dequeue()
print(f'Atendido: {atendido}')

# Verifica quem será o próximo, sem retirá-lo da fila
proximo = fila.peek()
print(f'Próximo: {proximo}')

# Imprime os elementos da fila
print(fila)

# Novas pessoas entram na fila
fila.enqueue('Bruno')
fila.enqueue('Bruna')
fila.enqueue('Bruno')

# Imprime os elementos da fila
print(fila)
