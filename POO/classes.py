#-*- coding: utf-8 -*-
class MinhaClasse: #declaração de classe
  x = 10

o = MinhaClasse() #declaração de objeto
print(o.x)

class Pessoa:
  def __init__(self, nome, idade): #função init atribui valores as propriedades do objeto
    self.nome = nome
    self.idade = idade

p1 = Pessoa("Primavera", 19)

print(p1.nome)
print(p1.idade)
print(p1)

class Fruta:
  def __init__(self, nome, tamanho):
    self.nome = nome
    self.tamanho = tamanho

  def __str__(self):
    return f"{self.nome}({self.tamanho})"    

f1 = Fruta("abacate", 25)

print(f1)
