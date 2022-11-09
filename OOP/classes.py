#-*- coding: utf-8 -*-
import datetime

class MinhaClasse: #declaração de classe
  x = 10

o = MinhaClasse() #declaração de objeto

print("----------declaração de objeto----------")
print(o.x) #

class Pessoa:
  #Função __init__ faz a iniciação do objeto em conjunto com o metodo cosntrutor __new__ que é chamado automaticamente sem a necissade de declaração.
  #A função __init__ não é a função construtora em si.
  
  
  def __init__(self, nome, idade):
    self.nome = nome              #Self.nome é uma caracteristica de Pessoa e ela recebe o valor "nome" 
    self.idade = idade            #Self faz referencia a classe, definindo que variaveis atribuitas com a sintaxe "self.xxx"-
                                  #São caracteristicas da classe e não apenas variaveis gerais; o uso explicitamente da palavra self não é obrigatorio, mas é uma boa prática.
                                  #É necessario self para parametros em argumetos para o objeto.
 
  def exemplo(proprio,x,y):#exemplo que que self é uma boa pratica 
    proprio.x = x
    proprio.y = y
    return ("funcionou " +str(x)+" "+str(y))

p1 = Pessoa("ANA", 19)

print("----------atributos de classe em objeto----------")
print(p1.nome)
print(p1.idade)
print("----------exemplo de que self é uma boa pratica----------")
print(p1.exemplo(1,2))
print(p1) #é assim que um objeto se parece sem o metodo __str__. Na ausencia do metodo __str__ o python chama o metodo __repr__

#representação de objetos em string.
print ("----------metodo __str__ ----------")
class Fruta:
  def __init__(self, nome, tamanho):
    self.nome = nome
    self.tamanho = tamanho

  def __str__(self):
    return f'{self.nome}({self.tamanho})'    # f-strings python 3.6 ou posterior 

f1 = Fruta("abacate", 25)
f2 = Fruta("laranja", 15)

print(f1)
print(f2)

print ("----------metodo __repr__ ----------")
class Livro:
  def __init__(self, nome, autor, ano):
    self.nome = nome
    self.autor = autor
    self.ano = ano
  def __repr__(self): 
      return f'Livro({self.nome}{self.autor}{self.ano})' 
  def idade(self): #metodo idade
    livroIdade = datetime.datetime.now().year - self.ano
    return livroIdade

livro1 = Livro("Dom Quixote","Miguel de Cervantes",1625)
print(livro1)
print("----------modificando atributos de objetos----------")
livro2 = Livro("antologia poética","Carlos Drummond de Andrade",1962)

print(livro2.nome)
print(livro2.autor)
print(livro2.ano)

print ("----------depois----------")
livro2.autor = "Vinicius de Moraes" # aqui alteramos o atributo autor
livro2.ano = 1954

print(livro2.nome)
print(livro2.autor)
print(livro2.ano)

del livro2.ano #deletando atributos de objetos
#print(livro2) ->aqui um erro ocorre por não possuir mais o parametro ano
livro2.ano = 1954 #atribuindo ano para continuar os tópicos

class Vazia: #definições de classe não podem ser vazios, faz necessario o uso do Statment pass
  pass

print ("----------invocando metodo----------")
print(livro1.idade())
