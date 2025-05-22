#!/usr/bin/python
# -*- coding: utf-8 -*-

# OPERADORES ARITIMÉTICOS
a = 2 + 2
s = 2 - 2
d = 2 / 2
m = 2 % 2  # resto da divisão
e = 2**2
f = 9 // 2  # divisão inteira sem resto
print("aritiméticos", a, s, d, m, e, f)

# ATRIBUIÇÃO
print("----atribuição----")
atribuicao = 10
print(atribuicao)
atribuicao += 1
print(atribuicao)
atribuicao -= 1
print(atribuicao)
atribuicao /= 1
print(atribuicao)
atribuicao %= 1
print(atribuicao)
atribuicao //= 1
print(atribuicao)
atribuicao **= 1

# COMPARAÇÃO
print("----comparação----")
x, y = 1, 2
print(x == y)  # igualdade
print(x != y)  # não igual
print(x < y)  # menor
print(x > y)  # maior
print(x <= y)  # menor ou =
print(x >= y)  # maior ou =

# OPERADORES LOGICOS
print("----operadores logicos----")

# operador (AND) retorna valor (TRUE) se os dois "statements" forem (TRUE)
print(x < 2 and x < 3)
print(x != 2 and x < 1)

# operador (OR) retorna (TRUE) se um dos "statements" é (TRUE)
print(x != 2 or x < 1)

# operador (NOT) reverte o resultado booleano
print(not (x != 2 or x < 1))

# OPERADORES DE IDENTIDADE
# operadores que servem para compração de objetos, não o mesmo valor mas a exata mesma alocação na memoria(se são iguais)
print("----operadores de identidade----")
x, y = 512, 512
m, n = ["pessoa", "animal"], ["pessoa", "animal"]

print(
    x is y
)  # o interpretador python aloca o mesmo endereço para as duas variaveis, por isso o is retorna true(similar a ponteiros)
print(m is n)  # o mesmo não é valido nesse caso e o is opera como esperado
print("teste ", m == n)  # os valores são exatamente iguais

print(x is not y)
print(m is not n)

# OPERADORES DE ASSOCIAÇÃO
# operadores que verificam se um objeto contém uma determianda sequência
print("----operadores de associação----")
p, f = "pessoa", "fruta"
print(p in m)
print(p in n)
print(f in m)
print(f in n)

print(f not in m)
print(f not in n)
