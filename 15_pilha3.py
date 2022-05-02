from lib.stack import Stack

analisador = Stack()

expr = 'x + (9 - ((y * 2) / 2) + 1)'

tem_erro = False

# Percorrer a expressão em busca de parênteses
for pos in range(len(expr)):
    if expr[pos] == '(':
        analisador.push(pos)
    elif expr[pos] == ')':
        # Se a ukha estiver vazia, temos um erro
        if analisador.is_empty:
            print(f'ERRO: fecha parêntese da posição {pos} não tem o abre correspondente')
            tem_erro = True
        else:
            # Tira a posição do abre da pilha
            pos_abre = analisador.pop()
            print(f'Abre parêntese da posição {pos_abre} corresponde ao fecha parêntese da posição {pos}')

while not analisador.is_empty:
    pos_abre = analisador.pop()
    print(f'ERRO: abre parêntese da posição {pos_abre} não tem fecha parêntese correspondente')
    tem_erro = True

#  Verifica se há sobra na pilha
if not tem_erro:
    print('*** PARÊNTESES CORRETAMENTE BALANCEADOS ***')



