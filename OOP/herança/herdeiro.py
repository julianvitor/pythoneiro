# -*- coding: utf-8 -*-
from nome import *
from estudante import *
from funcionario import *
from professor import *

print("---------objeto e de Estudante---------")
e = Estudante("José", "Carvalho") #objeto da classe Estudante que é filha/herdeira de Nome
e.printnome() #metodo especifico da classe Nome

print("---------objeto f de funcionario---------")
f = Funcionario("Lucia", "Vargas","EEEFM") #objeto classe funcionario
f.printnome() #metodo especifico da classe Nome (pai)
f.printescola() #metodo especifico da classe funcionario

print ("----------herança super()----------")
print ("----------objeto p de Professor----------")

p = Professor("Janaina", "Grogan","EEEFM", "filosofia")
p.printdisciplina() #metodo especifico da classe professor
