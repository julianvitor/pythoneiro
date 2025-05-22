#!/usr/bin/python
# -*- coding: utf-8 -*-
"variavel em unica linha"

x, y, z = 1, 2, 3
print(x, y, z)

# variavel em multiplas linhas
x = 1
y = 2
z = 3
print(x, y, z)

# desempacotar coleção em variavel
numeros = [1, 2, 3]
x = y = z = numeros
print(x, y, z)


# variavel global dentro de função
def myfunc():
    global x
    x = "global"


myfunc()
print(x)

# del é capaz de remover uma variavel
a = 512
print(a)
print("aqui passamos o del")

del a

if "a" in locals():
    print('"a" ainda está aqui')
else:
    print('"a" se foi')
