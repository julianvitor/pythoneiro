# -*- coding: utf-8 -*-

#criando uma função para usar decorator
def Dprint(funcao): #o parametro função é a função imediatamente abaixo do decorator
    def wrapper():
        funcao()    
        print(funcao()) #funcionalidade extra
    return wrapper

@Dprint #decorator, adicionando funcionalidade extra a função
def SomaCinco():
    resultado = 5+5
    return resultado

SomaCinco()