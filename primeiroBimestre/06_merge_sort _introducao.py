lista = [7, 4, 2, 6, 0, 3, 9, 1, 5, 8]

#Acha o meio da lista:
meio = len(lista) // 2 # // (divisão inteira)

metade1 = lista[0:meio]
metade2 = lista[meio:]

print(f'Lista {lista} \nMeio: {meio} \nMetade 1: {metade1} \nMetade 2: {metade2}')


