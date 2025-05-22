# -*- coding: utf-8 -*-
try:
    b = a + 2
except:
    print("um erro ocorreu")

print("--------multiplas exceções--------")
try:
    print(b=a + 2)
except NameError:  # except especifico
    print("um erro ocorreu: variavel não definida")

except:  # qualquer outro except
    print("um erro ocorreu")

print("--------try com else--------")
try:  # tente e execute o seguinte codigo
    print(5 + 5)

except:  # caso ocorra um erro
    print("ocorreu um erro")

else:  # caso nenhum erro ocorra o corigo no bloco try é executado e logo após o bloco else
    print("Sucesso")

print("----------finally----------")
try:
    print(b=a + 2)
except NameError:
    print("um erro ocorreu: variavel não definida")
finally:  # independende do try o finally é executado
    print("final do bloco")
