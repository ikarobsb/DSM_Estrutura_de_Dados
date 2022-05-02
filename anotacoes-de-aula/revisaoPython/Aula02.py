from turtle import clear


frutas = ['laranja', 'maçã', 'uva', 'pera', 'mamão', 'abacate', 'amora']
#           0           1       2       3       4       5           6

# Imprimindo o terceiro elemento:
print(f'Fruta da terceira posição {frutas[2]}')

# Substituindo "pêra" por "melancia":

frutas[3] = 'melancia'

print(frutas)

print('-' * 25)

# Percorrendo a lista eibindo os seus elementos do primeiro ao último
for f in frutas:
    print(f, end=', ')

# Percorrendo a lista e exibindo os seus elementos do último para o primeiro ao
print('\n')
for f in reversed(frutas):
    print(f, end=', ')

print('\n')
print('-' * 25)

# Percorrendo a lista e exibindo os seus elementos e a sua posição da lista.
print('\n')
for i in range (len(frutas)): #len() mede o comprimento de uma lista ou string, ou seja vai contar de 0 a última
    print(f'{i}: {frutas[i]}') # f'{} alguma coisa' é o mesmo que 'alguma cois {}'.format()

# Percorrendo a lista e exibindo os seus valores e posições, porém invertido (muito raramente iremos utilizar):
print('-' * 25)
for i in range (len(frutas) -1, -1, -1): #len(frutas)-1, para exibir a posição 6, pois len(frutas) == 7
    print(f'{i}: {frutas[i]}')
