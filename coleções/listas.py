#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import remove

# lista é um dos Tipos com capacidade de armazenar diversos dados
lista = ["feliz", "tiste", "catatônico", "feliz", "tiste", "catatônico"]
listaNumerica = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
print(lista)
print(listaNumerica)

# é possivel navegar pelo indice em listas
print(lista[2])
print(listaNumerica[4])

# len
print(len(listaNumerica))

# listas tambem são classes, <class'listaNumerica'>
print(type(listaNumerica))

# list() para criar uma lista a partir de uma tupla
listaGrande = list(("caneta", "lapis", "borracha"))
print(listaGrande)

# existem outros tipos de coleções em python
""">List is a collection which is ordered and changeable. Allows duplicate members.
   >Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
   >Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
   >Dictionary is a collection which is ordered** and changeable. No duplicate members."""

# assim como nos exemplos de string é possivel manipular listas de diversas formas, confira na documentação
listaGrande[0] = "cachorro"
print(listaGrande)

# insert adiciona intens em pontos determinados da lista
listaGrande.insert(1, "gato")
print(listaGrande)

# append adiciona intens ao final da lista
listaGrande.append("coelho")
print(listaGrande)

# extend adiciona itens de coleções em outras listas
listaGrande.extend(lista)
print(listaGrande)

# remove
listaGrande.remove("coelho")
print(listaGrande)

# pop remove um index especifico
listaGrande.pop(0)
print(listaGrande)

# del pode apagar uma lista completa(del listaGrande)
listinha = ["pequena", "lista"]
del listinha  # some a listinha
if "listinha" in locals():
    print('"listinha" ainda está aqui')
else:
    print('"listinha" se foi')

# clear
listinhaTemporaria = ["pequena", "lista"]
listinhaTemporaria.clear()
print(listinhaTemporaria)

# loop assim como em strings
listaGrande
for x in listaGrande:
    print(x)

# loop pelos indices
print("_____loop pelos indices_____")
for i in range(len(listaGrande)):
    print(listaGrande[i])

# while loop
print("_____while_____")
contador = 0
tamanhoLista = len(listaGrande)
while contador < tamanhoLista:
    print(listaGrande[contador])
    contador += 1

# comprehension é um recurso para encurtar a forma sintatica, confira na documentação.
# comprehension loop
print("comprehension")
[print(x) for x in listaGrande]

# comprehension com condicional
novalistaGrande = [x.upper() for x in listaGrande if "a" in x]
print(novalistaGrande)

# sort() ordena listas
listaGrande.sort()
print(listaGrande)

listaNumerica.sort()
print(listaNumerica)

listaNumerica.sort(reverse=True)
print(listaNumerica)

listaGrande.sort(key=str.lower)  # case sensitive
print(listaGrande)

# reverter a lista
listaNumerica.reverse()
print(listaNumerica)

listaNumerica.sort(reverse=True)
print(listaNumerica)


# key definida por função
def myFunc(u):
    return abs(u - 2)


listaNumerica.sort(key=myFunc)  # lista ordenada proximado de 2
print(listaNumerica)

# copiar listas
# copiar lista com operador de atribuição implica que mudanças na primeira lista inflenciara na segunda lista
novaListaNumerica = listaNumerica.copy()
listaNumerica.append(6)
print(listaNumerica)
print(novaListaNumerica)

# outra forma de concatenar listas
listao = listaGrande + listaNumerica
print(listao)
