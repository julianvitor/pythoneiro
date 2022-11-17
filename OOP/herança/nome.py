# -*- coding: utf-8 -*-
class Nome:# classe pai
  def __init__(self, primeiroNome, ultimoNome):
    self.primeiroNome = primeiroNome
    self.ultimoNome = ultimoNome

  def printnome(self):
    print(self.primeiroNome, self.ultimoNome)