# -*- coding: utf-8 -*-
from nome import *


class Funcionario(Nome):  # classe herdeira de Nome
    def __init__(
        self, primeiroNome, ultimoNome, escola
    ):  # define uma nova função __init__ substituindo a __init__ da classe pai repare no parametro "escola" que é novo
        Nome.__init__(
            self, primeiroNome, ultimoNome
        )  # faz uma chamada da função __init__ da classe Nome para a reutilizar, repare nos parametros "primeiroNome" e "ultimoNome" que são antigos, -
        # self.printnome e self.ultimoNome não são necessarios
        self.escola = escola

    def printescola(self):  # metodo especifico da classe funcionario
        print(self.escola)
