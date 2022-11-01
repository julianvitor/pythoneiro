# -*- coding: utf-8 -*-
logadouro = ["rua", "avenida", "alameda"]
for i in logadouro:
    print(i)

for i in "string":
    print(i)

print("---------break---------")
logadouro = ["rua", "avenida", "alameda"]
for i in logadouro:
    print(i)
    if i == "avenida":
        break
print("---------break----------")

for i in logadouro:
    if i == "avenida":
        continue        #pular o loop atual
    print(i)

for x in range(0,11,2):
    print(x)

logadouro = ["rua", "avenida", "alameda"]
for i in logadouro:
    print(i)
else: 
    print("fim do loop")

#for encadeado
construcao = ["casa", "apartamento", "sobrado"]
for i in logadouro:
    for j in construcao:
        print(i,j)

for i in "vazio": #necessario pass para não apresentar erro em loop vazio
    
    pass
#comprehension 
listaGrande = ["a","e","i","o","u"] 
[print(x) for x in listaGrande] 

