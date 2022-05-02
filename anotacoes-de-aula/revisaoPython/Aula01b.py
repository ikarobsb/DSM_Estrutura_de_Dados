# Função range()

# 1) Com apenas um argumento, range() cria uma lista que vai de 0 (\ero) até o argumento

for i in range(10):
    print(i, end=' ')

# 2) range() com 2 argumentos: gera uma lista partindo do primeiro valor até o último

print('\n------------------')

for x in range (5, 15):
    print(x, end=' ')

# 3) range() com três argumentos 1) início, 2) final, 3) de quantos em quantos vai pular
print('\n------------------')
for c in range (1,10,2):
    print(c, end=' ')

# 4) range() regredindo
print('\n--------------------------')
for k in range (10, -1, -1):
    print(k, end=' ')