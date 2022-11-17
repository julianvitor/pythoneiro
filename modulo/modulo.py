#-*- coding: utf-8 -*-

pessoa = {
    "nome":"Pedro",
    "email":"pedro@gmail.com",
    "senha":"batata"
}

class Contar:
  def __iter__(self): #metodo que cria o objeto iterador e inicializa a classe
    self.controle = 0
    return self       #sempre deve retornar o proprio objeto iteravel

  def __next__(self):
    if self.controle < 11:
      item = self.controle
      self.controle += 1
      return item #retorno do proximo item da sequencia
    else:
      raise StopIteration #sem essa condicional o loop rodaria ad aeternum

def iterador():
    iteradorModulo = iter(Contar())
    for i in iteradorModulo:
        print (i)


