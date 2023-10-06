# -*- coding: utf-8 -*-

#criando uma função para usar decorator
def Dprint(funcao): #o parametro função é a função imediatamente abaixo do decorator no nosso caso "SomaCinco()"
    def wrapper():
        funcao()    
        print(funcao()) #funcionalidade extra
    return wrapper

@Dprint #decorator, adicionando funcionalidade extra a função
def SomaCinco():
    resultado = 5+5
    return resultado

SomaCinco()

def meu_decorator(funcao):
    def wrapper():
        print("Antes da execução da função")
        funcao()
        print("Depois da execução da função")
    return wrapper

@meu_decorator
def minha_funcao():
    print("Função original")

minha_funcao()
