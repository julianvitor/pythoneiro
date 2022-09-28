#!/usr/bin/python
# -*- coding: utf-8 -*-

#numeros
x,y,y2,z = 1, 1.0, 1E10, 1j
print (type(x),type(y),type(y),type(z))

#conversão 
x = float(x)
y = str(y)
y2 = complex(y2)
z = str(z) #complexos não podem ser convertidos para outros formatos de numeros
print(type(x), type(y), type(y2), type(z))

#cast
x,y,z = 1, 1.5, 2.9
print (float(x))
print (int (y))
print (int (z))

