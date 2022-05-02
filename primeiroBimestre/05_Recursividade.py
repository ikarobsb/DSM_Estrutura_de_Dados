# Recursividade:
# 6! = 6 * 5!
# 5! = 5 * 4! e assim por diante, ou seja, n! = n * (n-1)! para n > 1
# 1! = 1 e 0! = 1 por definição
# 'Recursividade' é um termo usado de maneira mais geral para descrever o processo de repetição de um objeto de um jeito similar ao que já fora mostrado. Um bom exemplo disso são as imagens repetidas que aparecem quando dois espelhos são apontados um para o outro. 

# Implementação iterativa de um fatorial
def fatorial_iter(n):
    resultado = 1
    for i in range(n, 1, -1):
        resultado *= i
    return resultado
print('Fatorial por função iterativa')  
num = 6; 
print(f'Fatorial de {num} é {fatorial_iter(num)}')

####################################################################

# Implementação recursiva de um fatorial
def factorial_rec(n): 
    if n == 1 or n == 0: # condição de saída OBS quando não se coloca um ponto de parada para a pilha de chamadas (no caso da def factorial_rec) é a opção do if, ocorre o estouro de pilha ou em inglês stack over flow
        return 1  
    elif n > 1: 
        n * factorial_rec(n - 1) # vc quer saver o fatorial de n, é só calcular n * o fatorial de n - 1  (pilha de chamadas)
    else: #números negativos
        return None # Outra condição de saída

print('Fatorial por função recursiva')    
num = 5; 
print(f'Fatorial de {num} é {fatorial_iter(num)}')

#########Função de Fatorial recursivo sem condição de saída para provocar ##################################Stack Over Flow#######################################

def fatorial_overflow(n):
    return n * fatorial_overflow(n-1)

