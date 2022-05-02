"""
    ESTRUTURA DE DADOS (STACK)
    É uma estrutura de dados linear em que tanto a operação de inserção (puch) quanto a operação de remoção/retirada (pop) acontecem ao final (ou topo).

    Como consequência, o fincionamento da pilha pode ser definido como LIFO (Last In First Out) ou FILO (First In Last Out).
"""

# Usando uma pilha rudimentar para inverter um texto.

texto = 'SOCORRAM ME SUBI NO ONIBUS EM MARROCOS'

# Em Python, é possível fazer com que uma lista se comporte como uma pilha.

pilha = []

# Colocando cada uma das letas do texto no final da pilha

for letra in texto:
    pilha.append(letra)

print(pilha)

inverso = ''

while len(pilha) > 0:
    retirado = pilha.pop()
    inverso += retirado

print(inverso)