#-*- coding: utf-8 -*-
import datetime
from rich import print

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

class Vazia: pass #definições de classe não podem ser vazios, faz necessario o uso do Statment pass

print ("----------invocando metodo----------")
print(livro1.idade())

print("---------herança---------")
class Nome:# classe pai
  def __init__(self, primeiroNome, ultimoNome):
    self.primeiroNome = primeiroNome
    self.ultimoNome = ultimoNome

  def printnome(self):
    print(self.primeiroNome, self.ultimoNome)

n = Nome("Pedro", "Laranja")
n.printnome()

class Estudante(Nome): pass #classe herdeira que utiliza a função __init__ da classe pai e seus metodos

e = Estudante("José", "Carvalho")
e.printnome()

print("----------herdeira chamada __init__ pai----------")
class funcionario(Nome): #classe herdeira de Nome
  def __init__(self, primeiroNome, ultimoNome, escola): #define uma nova função __init__ substituindo a __init__ da classe pai repare no parametro "escola" que é novo
    Nome.__init__(self, primeiroNome, ultimoNome) #faz uma chamada da função __init__ da classe Nome para a reutilizar, repare nos parametros "primeiroNome" e "ultimoNome" que são antigos
    self.escola = escola

  def printescola(self): #metodo especifico da classe funcionario
    print(self.escola)

f = funcionario("Lucia", "Vargas","EEEFM")
f.printnome()
f.printescola() #metodo especifico da classe funcionario

print ("----------herança super()----------")
class professor(funcionario): #classe herdeira de funcionario
  def __init__(self, primeiroNome, ultimoNome, escola, disciplina): #define uma nova função __init__ substituindo a __init__ da classe pai repare no parametro "escola" e "disciplina"
    super().__init__(primeiroNome, ultimoNome, escola) #
    self.disciplina = disciplina

  def printdisciplina(self): #metodo especifico da classe professor
    print(self.disciplina)

p = professor("Janaina", "Grogan","EEEFM", "filosofia")
p.printdisciplina() #metodo especifico da classe professor

print ("---------iterador e iteravel---------")
#exemplo de um objeto iterador
lista = "exemplo"
for i in lista: #o loop for cria um objeto iterador e executa o metodo next() para cada loop
  print(i)

print("----------criando um iterador----------")
#criando um iterador

class Contar:
  def __iter__(self): #metodo que cria o objeto iterador e inicializa a classe
    self.a = 0
    return self       #sempre deve retornar o proprio objeto iteravel

  def __next__(self):
    x = self.a
    self.a += 1
    return x #retorno do proximo item da sequencia
  
c = Contar()
iterador = iter(c)
print(next(c))
print(next(c))
print(next(c))

print("----------criando um iterador limitado----------")

class Contar2:
  def __iter__(self): #metodo que cria o objeto iterador e inicializa a classe
    self.a = 0
    return self       #sempre deve retornar o proprio objeto iteravel

  def __next__(self):
    if self.a < 3:
      x = self.a
      self.a += 1
      return x #retorno do proximo item da sequencia
    else:
      raise StopIteration #sem essa condicional o loop rodaria ad aeternum

iterador2 = iter(Contar2())
for i in iterador2:
  print (i)