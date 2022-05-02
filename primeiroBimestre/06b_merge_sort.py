from data.nomes_desord import nomes

# ALGORITMO DE ORDENAÇÃO MERGE SORT

# No processo de ordenação, esse algoritmo "desmonta" o vetor original contendo N elementos até obter N vetores de aoenas um elemento cada um.
# Em seguida, usando a técnica de mesclagem (merge), "remonta" o vetor, dessa vez com os elementos já em ordem.

divs = juncoes = comps = 0

def merge_sort(lista):
    
    global divs, juncoes, comps

    # Só continua se o comprimento da lista for maior que 1.
    if len(lista) <= 1:
        return lista
    
    # Encontra a posição do meio da lista
    meio = len(lista) // 2

    # Cópia da primeira metade do vetor
    sublista_esq = lista[:meio]
    # Cópia da segunda metade do vetor
    sublista_dir = lista[meio:]

    divs += 1 #contando as divisões

    # Chamamos recursivamente a função para que ela continue repartindo cada uma das sublistas em metades
    sublista_esq = merge_sort(sublista_esq)
    sublista_dir = merge_sort(sublista_dir)

    # AQUI COMEÇA A JUNÇÃO DAS DIAS METADES DA LISTA, ORDENADAMENTE
    pos_esq = pos_dir = 0
    ordenada = [] # lista vazia

    # Compara os elementos da sublista entre si e insere na lista ordenada o que for menor

    while pos_esq < len(sublista_esq) and  pos_dir < len(sublista_dir):
        # O elemento que se encontra na posição da sulista esquerda é menor que o que se encontra na sublista direita
        comps += 1

        if sublista_esq[pos_esq] < sublista_dir[pos_dir]:
            ordenada.append(sublista_esq[pos_esq])
            pos_esq += 1
        # O contrário
        else:
            ordenada.append(sublista_dir[pos_dir])
            pos_dir += 1
    # Verificação da sobre
    sobra = []

    # Sobra a esquerda
    if pos_esq < pos_dir:
        sobra = sublista_esq[pos_esq:]
    # Sobra a direita
    else:
        sobra = sublista_dir[pos_dir:]

    # O resultado final é a concatenação da lista ordenada com a sobra 
    juncoes += 1
    return ordenada + sobra

#############################################################################################

divs = juncoes = comps = 0

nums = [7, 4, 2, 6, 0, 3, 9, 1, 5, 8]
resultado = merge_sort(nums)
print(f'{resultado} divisões = {divs} junções = {juncoes} comparações = {comps}')

# resultado = merge_sort(nomes)
# print(f'divisões = {divs} junções = {juncoes} comparações = {comps}')
