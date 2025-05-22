# -*- coding: utf-8 -*-


# criando uma função para usar decorator
def DecoratorPrint(
    funcao,
):  # o parametro função é a função imediatamente abaixo do decorator no nosso caso "SomaCinco()"
    def wrapper():
        print(funcao())  # funcionalidade extra

    return wrapper


@DecoratorPrint  # decorator, adicionando funcionalidade extra a função
def SomaCinco():
    resultado = 5 + 5
    return resultado


SomaCinco()

print("-----fim-----")


def AntesDepoisDecorator(funcao):
    def wrapper():
        print("Antes da execução da função")
        funcao()
        print("Depois da execução da função")

    return wrapper


@AntesDepoisDecorator
def minha_funcao():
    print("Função original")


minha_funcao()
