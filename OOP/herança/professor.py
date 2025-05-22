# -*- coding: utf-8 -*-
from funcionario import *


class Professor(Funcionario):  # classe herdeira de funcionario
    def __init__(
        self, primeiroNome, ultimoNome, escola, disciplina
    ):  # define uma nova função __init__ substituindo a __init__ da classe pai repare no parametro "escola" e "disciplina"
        super().__init__(
            primeiroNome, ultimoNome, escola
        )  # super() permite extender metodos da classe pai automaticamente, no nosso caso "Funcionario" Confira na documentação para detalhes.
        self.disciplina = disciplina  # nova varial da classe Professor

    def printdisciplina(self):  # metodo especifico da classe Professor
        print(self.disciplina)


objeto = Professor("pedro", "josias", "123", "matematica")  # criando um objeto
objeto.printdisciplina()  # chamando um metodo da classe Professor
