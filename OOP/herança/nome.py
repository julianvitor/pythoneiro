# -*- coding: utf-8 -*-
class Nome:  # classe pai
    def __init__(
        self, primeiroNome="generico", ultimoNome="generico"
    ):  # iniciador da classe, comumente confundida com função construtora
        self.primeiroNome = primeiroNome
        self.ultimoNome = ultimoNome

    def printnome(self):  # metodo de classe
        print(self.primeiroNome, self.ultimoNome)


objetonome = Nome("teste", "teste")
objetonome.printnome()
