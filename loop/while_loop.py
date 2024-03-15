# -*- coding: utf-8 -*-
a = 0 
while a != 10:
    print(a)
    a = a+1
    if a > 4:
        break
print("---------fim----------")

b = 0
while b < 6: 
    b += 1
    if b == 3:
        continue #pular iteracao atual assim como no exemplo do for
    print(b)
print("---------fim----------")

c = 0 
print(f"antes do while o valor de C é: {c}")
while c < 10:
    print(f"c:  {c}")
    c += 1
else: #O bloco else em um loop while é executado quando a condição do loop se torna falsa (ou quando o loop é interrompido por uma instrução break).
    print("else após while")
    print(c)
