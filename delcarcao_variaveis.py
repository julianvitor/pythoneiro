# -*- coding: utf-8 -*-
"variavel em unica linha"
x, y, z = 1, 2, 3
print(x,y,z)

#variavel em multiplas linhas
x = 1
y = 2 
z = 3
print(x,y,z)

#desempacotar coleção em variavel
numeros = [1,2,3]
x = y = z = numeros
print (x,y,z)

#variavel global dentro de função
def myfunc():
    global x
    x = "global"

myfunc()
print ()
