# -*- coding: utf-8 -*-

def primeira_funcao(): #declaração
    print("hello word")

#primeira_funcao()

print("v__________função com argumento___________v")

def segunda_funcao(nome): #<<<< parametro
    print(str(nome) + " Li") 

#segunda_funcao(str(input("Nome: ")))#<<<< argumento

print("__________numero de parametros desconhecido__________")

def terceira_funcao(*cidades): 
    print("a cidade de maior distancia é: "+ cidades[1])

#terceira_funcao("Londrina","Mauá","Santarém","Anápolis")
#terceira_funcao(cidade)

def quarta_funcao(nome1, nome2, nome3): #é possivel especificar os parametros no argumento independende da ordem utilizando chave-valor
  print("o menor deles é  " + nome3)

#quarta_funcao(nome1 = "piaba", nome2 = "peixe-lua", nome3 = "tilapia")

def quinta_funcao(**valor): #atribuição através de chave-valor sem esperar um numero de argumentos (def x(*y))
  print("o valor é " + valor["valor0"]) 

quinta_funcao(valor0 = "azul", valor1 = "vermelho")

