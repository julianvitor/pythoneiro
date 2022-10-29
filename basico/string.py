#!usr/bin/python
# -*- coding: utf-8 -*-
a = "string"
print (a)
print (a[1]) #posição em string (strings são arrays de bytes)

#loops podem ser usados em strings
for x in "string":
    print (x)

#tamanho de uma string
print (len(a))

#in
a = "paçoca, mariola, azeitona"
print ("paçoca" in a)

#if
if "azeitona" in a:
    print("sim, azeitona tambem está aqui.")
else:
    pass

#not in
print ("pamonha" not in a)

#if not in
if "pamonha" not in a:
    print("não, pamonha não tem.")
else:
    pass

#slicing
#é possivel retornar um intervalo de caracteres em uma string
print (a[:6])
print (a[8:15])
print (a[17:])
print (a[-8:])

#MAIUSCULO 
a = a.upper()
print (a)
#minusculo
a = a.lower()
print(a) 

#remover espaço no incio ou final do array
print(a.strip())

#substituir uma string
print (a.replace("m", "p"))

#separar o array em um determinado ponto
print (a.split(","))

#concatenar strings
c, d = "Batata", "Manga"
e = c + " " + d
print (e)

#formatar strings (é possivel formatar para concatenar em uma determinada posição)
quantiade = 100
ingredientes = "açucar, aspargos, torrone e talvez {}kg de alho"
print (ingredientes.format(quantiade))

#é possivel inserir chaves para especificar a posição
quantiade = 10
preço = 15.5
tipo = 2
instrução = "preciso de {1} tomates do tipo {0}, não quero pagar mais de R${2} "
print (instrução.format(tipo, quantiade, preço))

#caracter de fuga
#para inserir caracteres não validos em uma string é preciso usar um caracter de fuga.
print("uma filosofo uma vez disse \"para quem está se afogando jacaré é toco\"")
print("isso insere uma barra invertida \\ no texto")
print("isso insere uma\nquebra de linha")
print("\157\145") #valor ocatal
print ("\x6f\x65")#valor hex
print ("um\ttab")

#existem diversos metodos para strings na bibliotaca padrão do python, confira na documentação oficial
#alguns exemplos
print(a.capitalize())
print (a.center(50,"-"))
print (a.find("mariola"))

