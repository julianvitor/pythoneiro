# -*- coding: utf-8 -*-

#casos bool false.
print (bool(False))
print (bool(None))
print (bool(0))
print (bool(""))
print (bool(()))
print (bool([]))
print (bool({}))

class classe(): 
  def __len__(self): #função __len__ retorna valor falso.
    return 0
    
obj = classe()
print(bool(obj))

#casos boll true: todos.

#retorno em funções
def myFunction() :
  return True
print(myFunction())

#retorno em função if
def funcao() :
  return True

if funcao():
  print("1")
else:
  print("0!")
