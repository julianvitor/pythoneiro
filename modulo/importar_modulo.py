# -*- coding: utf-8 -*-
import platform  # exemplo de importação de modulo
import modulo  # importar modulo criado
import modulo2 as mod2  # renomear modulos
from modulo3 import convidado  # importar objeto expecifico

print("---------exemplo---------")
x = platform.system()
print(x)

print("----------importar função----------")
modulo.iterador()

print("----------importar objeto----------")
b = modulo.pessoa["email"]
print(b)

print("----------importar como...---------")
email = mod2.cliente["email"]
print(email)

print("--------importar objeto expecifico----------")
print(convidado["email"])

print("--------listar objetos----------")
print(dir(modulo))
