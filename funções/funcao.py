# -*- coding: utf-8 -*-

def zero_funcao(): #declaração
    print ("hello world")
zero_funcao()

def primeira_funcao(nome): #declaração
    print("hello "+ str(nome[0]))

nome = ("Londrina", "Mauá", "Santarém", "Anápolis")
primeira_funcao(nome)

def segunda_funcao(nome): #<<<< parametro
    print(str(nome) + " Li") 

segunda_funcao(str(input("Nome: ")))#<<<< argumento

def terceira_funcao(*cidades):  #usando (*parametro) é possivle passar uma tupla como argumento
    print("a cidade de maior distancia é: "+ str(cidades[1]))

terceira_funcao("Londrina", "Mauá", "Santarém", "Anápolis")

def quarta_funcao(nome1, nome2, nome3): #é possivel especificar os parametros no argumento independende da ordem utilizando chave-valor
  print("o menor deles é  " + nome3)

quarta_funcao(nome1 = "piaba", nome2 = "peixe-lua", nome3 = "tilapia")

def quinta_funcao(**valor): #atribuição através de chave-valor sem esperar um numero de argumentos (def x(*y))
  print("o valor é " + valor["valor0"]) 

quinta_funcao(valor0 = "azul", valor1 = "vermelho")

def sexta_funcao(comida = "pão"): #valor padrão ja interno na declaração da funcao para caso de não expecificação
    print("o almoço é " +comida)

sexta_funcao()
sexta_funcao("goiabada")
sexta_funcao("gorgonzola")

def setima_funcao(arte): #os tipos se mantem passando em uma função, (listas continuam sendo lista)
    [print(x) for x in filme]

filme = ["Que Horas Ela Volta?","Ônibus 174","O Som ao Redor", "O Senhor dos Anéis","Cidade de Deus"]
setima_funcao(filme)

def oitavafuncao(n):  
    return 3.14/n # retorno da função

print(oitavafuncao(30))

def nonafuncao(): #pass 
  pass

 #função recursiva, é possivel utulizar uma função como
 #parametro para outra função ou ela mesmo. Confira recursão para maior abordagem do assunto
def fatorial(numero):
    if numero == 1:
        return 1
    
    return numero * fatorial(numero - 1)

print(fatorial(4))
