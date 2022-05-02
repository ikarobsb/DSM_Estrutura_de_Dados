# Um dicionário é uma estrutura de dados fornecida pela linguagem Python capaz de armazenar múltiplos valores em uma única variável, por meio de pares de chave-valor.
# OBS: armazena apenas dados, nunca algoritmos.

pessoa = {
    # "nome" é a chave | "Íkaro" é o valor
    'nome': 'Íkaro',
    'sexo': 'M',
    'idade': 34,
    'peso': 70,
    'altura': 1.75
}

# Acessando os valores armazenados em um dicionário
print (f"Nome:  {pessoa['nome']}") # lembrar que temos que utilizar aspas duplas e simples ou vice versa.
print(f"Idade:  {pessoa['idade']}")

# Calculando o IMC:
imc = pessoa['peso'] / pessoa['altura'] ** 2

print(f'IMC: {imc}')

##############################################################################

