# -*- coding: utf-8 -*-
logadouro = ["rua", "avenida", "alameda"]
for i in logadouro:
    print(i)

print("---------fim---------")

for i in "string":
    print(i)

print("---------fim---------")

logadouro = ["rua", "avenida", "alameda"]
for i in logadouro:
    print(i)
    if i == "avenida":
        break

print("---------fim----------")

for i in logadouro:
    if i == "avenida":
        continue        #pular o loop atual
    print(i)

print("---------fim---------")

for x in range(0,11,2):
    print(x)
print("---------fim---------")

logadouro = ["rua", "avenida", "alameda"]
for i in logadouro:
    print(i)
else: 
    print("fim do loop")

print("---------fim---------")
#for encadeado
construcao = ["casa", "apartamento", "sobrado"]
for i in logadouro:
    for j in construcao:
        print(i,j)

print("---------fim---------")

for i in "vazio": #necessario pass para não apresentar erro em loop vazio
    
    pass
#comprehension 
listaGrande = ["a","e","i","o","u"] 
[print(x) for x in listaGrande] 

print("---------fim---------")
