# -*- coding: utf-8 -*-
class Profissao:
    def __init__(self, nome, salario):
        # Atributos privados com prefixo de dois underscores
        self.__nome = nome
        self.__salario = salario

    def get_nome(self):
        # Método de acesso para recuperar o nome da profissão
        return self.__nome

    def get_salario(self):
        # Método de acesso para recuperar o salário da profissão
        return self.__salario

    def set_nome(self, nome):
        # Método para alterar o nome da profissão
        self.__nome = nome

    def set_salario(self, salario):
        # Método para alterar o salário da profissão
        self.__salario = salario


# Exemplo de uso da classe
profissao = Profissao("Engenheiro de Software", 8000)
print(profissao.get_nome())  # saída: Engenheiro de Software

profissao.set_nome("Desenvolvedor Web")
print(profissao.get_nome())  # saída: Desenvolvedor Web
