# -*- coding: utf-8 -*-
# funções anônimas ou funções Lambda
# são funções que não
# recebem atribuição de nome, recebem diversos argumetos mas realizam apenas uma expressão.
# lambda parametro : expressão

x = lambda parametro: parametro + 10  # declaração e uso simples
print(x(35))


def myfunc(n):  # uso encadeado em outra função
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(5))
print(mytripler(11))
