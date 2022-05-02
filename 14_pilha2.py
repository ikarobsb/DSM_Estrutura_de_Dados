from lib.stack import Stack

# Cria uma pilha
pilha = Stack()

print('Pilha está vazia? ', pilha.is_empty)

# x = pilha.peek()

try:
    x = pilha.pop()
except:
    print('Aconteceu o erro de retirada da pilha vazia. Ignorando...')

pilha.push(12)
pilha.push(25)

try:
    x = pilha.peek()
except:
    print('Aconteceu o erro de retirada da pilha vazia. Ignorando...')

print('Pilha está vazia? ', pilha.is_empty)

print('x:', x)

print(pilha)

#####################################################

from data.lista_nomes import nomes

inversor = Stack()

# Empilhar cada um dos nomes na pilha inversora
for nome in nomes:
    inversor.push(nome)

nomes_inverso = []

# À medida que desempilha do inversor, coloca os
# nomes em nomes_inverso
while not inversor.is_empty:
    nomes_inverso.append(inversor.pop())

# Exibe os 100 primeiros nomes de nomes_inverso
print(nomes_inverso[:100]) 