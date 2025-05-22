# -*- coding: utf-8 -*-

# tuplas são ordenadas e imutaveis mas permitem itens duplicados.
tupla1 = ("batata",)
tupla2 = ("batata", "espinafre", "couve", "batata")
print(tupla1)
print(tupla2)
# funções de listas geralemnte funcionam em tuplas, seguindo claro sua natureza imutavel
print(len(tupla2))

# para o python tuplas são objetos do tipo tupla. <class 'tuple'>
print(type(tupla2))

# metodo construtor
tupla3 = tuple(("avião", "carro", "motocicleta"))
print(tupla3)

# é possivel converter tupla para listas e assim poder a alterar como lista
print("----------conversão ----------")
lista = list(tupla3)
lista[0] = "bicicleta"
tupla3 = tuple(lista)
print(tupla3)

# unpacking, atribuir elementos da tupla em variaveis.
print("----------unpacking----------")
(x, y, z) = tupla3
print(x)
print(y)
print(z)

# unpacking com * (atribui tipo de lista para a variavel com asterisco, contendo os itens alem do numero do indice )
print("---unpacking com *---")
(x, *y) = tupla3
print(x)
print(y)
print(tupla3)
