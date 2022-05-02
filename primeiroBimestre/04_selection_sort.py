# O Selection Sort segue uma rotina bem simples e direta: encontrar o menor elemento e colocá-lo na primeira posição. A ordenação nada mais é do que aplicar essa rotina repetidas vezes para o restante do array. O Selection sort é in-place e O(n2). A implementação clássica do Selection Sort não é estável.
from data.nomes_desord import nomes
from time import time

passadas = comps = trocas = 0


def selection_sort(lista):

    global passadas, comps, trocas
    passadas = comps = trocas = 0

    def encontrar_pos_menor(pos_ini, pos_fim):
        global comps
        pos_res = pos_ini
        #Loop da segunda até a última posição 
        for pos in range(pos_ini + 1, pos_fim + 1):
            comps += 1
            if lista[pos] < lista[pos_res]:
                pos_res = pos 
        return pos_res

    #loop que vai da primeira até a penúltima posição
    for pos_sel in range(len(lista) - 1):
        passadas += 1
        #Encontra o menor valr na faixa entre o número seguinte a pos_sel e o fim da lista
        pos_menor = encontrar_pos_menor(pos_sel + 1, len(lista) - 1)

        #compara se o menor valor encontrado é ainda menor que o valor da posição selecionada
        comps += 1
        if lista[pos_menor] < lista[pos_sel]:
            #Efetua a troca
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor]
            trocas += 1

nums = [7, 4, 2, 9, 0, 6, 5, 3, 1, 8]
nums2 = [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]
# Pior caso do selection sort = 9, 0, 1, 2, 3, 4, 5, 6, 7, 8

selection_sort(nums2)
print(nums2)
print(f'Passadas: {passadas}; Comparações {comps}; Trocas: {trocas}')

