#-*- coding: utf-8 -*-
class MinhaClasse: #declaração de classe
  x = 10

o = MinhaClasse() #declaração de objeto
print("---declaração de objeto---")
print(o.x) #

class Pessoa:
  #Função __init__ faz a iniciação do objeto em conjunto com o metodo cosntrutor __new__ que é chamado automaticamente sem a necissade de declaração.
  #A função __init__ não é a função construtora em si.
  #Self.nome é uma caracteristica de Pessoa e ela recebe o valor "nome" 
  #Self faz referencia a classe, definindo que variaveis atribuitas com a sintaxe "self.xxx"-
  #São caracteristicas da classe e não apenas variaveis gerais; o uso explicitamente da palavra self não é obrigatorio, mas é uma boa prática.
  #É necessario self para passar parametros para o objeto.
  def __init__(self, nome, idade):
    self.nome = nome               
    self.idade = idade             
  def exemplo(proprio,x,y):#exemplo que que self é uma boa pratica 
    proprio.x = x
    proprio.y = y
    return ("funcionou " +str(x)+" "+str(y))

p1 = Pessoa("ANA", 19)
print("---atributos de classe em objeto---")
print(p1.nome)
print(p1.idade)
print(p1)
print("---exemplo de que self é uma boa pratica---")
print(p1.exemplo(1,2))

print ("---função __str__---")
class Fruta:
  def __init__(self, nome, tamanho):
    self.nome = nome
    self.tamanho = tamanho

  def __str__(self):
    return f"{self.nome}({self.tamanho})"    

f1 = Fruta("abacate", 25)
f2 = Fruta("laranja", 15)
print(f1)
print(f2)
