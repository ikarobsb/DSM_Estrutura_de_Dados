from lib.doubly_linked_list import DoublyLinkedList

lista = DoublyLinkedList()

lista.insert(90, 'Jhonas') # posição informada é ignorada
lista.insert_head('Rafael') # inserção no início
lista.insert_tail('Maria') # inserção no final
lista.insert(2, 'Pedro') # inserção na posição 2
lista.insert(lista.count, 'Paulo') # inserção na última posição
lista.insert(0, 'Ana') # inserção na primeira posição

print(lista)
