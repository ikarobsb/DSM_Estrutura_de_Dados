# Classe é uma estrutura que representa conjuntamente dados (variáveis) e algoritmos (na forma de funções). Uma classe é como uma "forma de bolo" com a qual se pode criar diferentes "bolos" (objetos), variando os "ingredientes" (dados) e o "modo de fazer" (algoritmos). Apesar dessa variação, os objetos criados a partir da classe sempre terão o formato determinado por esta.

from math import pi


class FormaGeometrica:

    # Uma classe pode ter dentro de si tanto dados quanto funções (estas representaod algoritmos). Uma função especial, denominada __init__, é chamada sempre que um novo objeto é criado a partir da classe, sendo conhecida como CONSTRUTOR.
    # Quando estão dentro de uma classe, as funções passam a ser chamadas MÉTODOS, e *SEMPRE* têm self como primeiro parâmetro, representando o próprio objeto.
    # parâmetro, representando o próprio objeto:
    def __init__(self, base, altura, tipo): # CONSTRUTOR

        # Recebemos os parâmetros no construtor e armazenando dentro do objeto que está sento criado. Utilizando-se de dois underlines antes do título do atributo Python considera o atributo como PRIVADO e portanto imutável.
        self.base = base
        self.altura = altura
        self.tipo = tipo

    # Propriedades

    @property           # Anootation
    def base(self):     # getter disfarçado
        return self.__base

    @base.setter        # Anotation
    def base(self, valor):  # setter disfarçado
        if type(valor) not in (int, float) or valor <= 0:
            raise Exception('A base deve ser numérica e maior que zero')
        self.__base = valor
    
    @property
    def altura(self): 
        return self.__altura

    @altura.setter
    def altura(self, valor):
        if type(valor) not in (int, float) or valor <= 0:
            raise Exception('A altura deve ser numérica e maior que zero')
        self.__altura = valor
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, valor):
        if valor not in ("R", "T", "E"):
            raise Exception('Tipo deve ser R, T ou E')
        self.__tipo = valor

###########################################################################################################

# Método para cálculo da área da formato

@property
def area(self):
    from math import pi 
    if(self.tipo == 'R'):   # Retângulo
        return self.base * self.altura
    elif(self.tipo == 'T'): # Triângulo
        return self.base * self.altura / 2
    else: # Elipse
        return pi * (self.base / 2) * (self.altura / 2)
    

# Criando objetos a partir da classe

forma1 = FormaGeometrica(12, 10, 'R')
forma2 = FormaGeometrica(7.5, 8.2, 'T')

# forma1.set_base("farinha")

print(f'Forma1 base: {forma1.base}, altura {forma1.altura}, tipo {forma1.tipo}, área {forma1.area}cm²')

print(f'Forma2 base: {forma2.base}, altura {forma2.altura}, tipo {forma2.tipo}, área {forma2.area:.2f}cm²')