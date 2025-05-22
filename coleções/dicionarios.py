# -*- coding: utf-8 -*-

# dicionarios armazenam dados no formato chave:valor.
# dicionarios são ordenados a partir da versão 3.7, são mutaveis e não permitem duplicatas.
dicionario = {"marca": "volkswagen", "modelo": "jetta", "ano": 2011}
print(dicionario)

# valor através da chave
item = dicionario["ano"]
print(item)
x = dicionario.get("marca")
print(x)


# valor duplicado substitui valor original
dicionario = {
    "marca": "volkswagen",
    "modelo": "jetta",
    "ano": 2011,
    "ano": 2022,
}
print(dicionario)

# dicionarios são objetos do tipo <classs 'dict'>
print(type(dicionario))

# keys() retornando todas as chaves (chaves sempre estão atualizadas na variavel atribuida)
x = dicionario.keys()
print(x)
dicionario["cor"] = "preto"
print(x)

# values(), retorno dos valores (valores sempre estão atualizados na variavel atribuida)
x = dicionario.values()
print(x)

# items(), retorno dos itens em tuplas dentro de uma lista, sempre atualizados
x = dicionario.items()
print(x)

# verificar se uma chave existe
if "cor" in dicionario:
    print("sim, cor está no dicionario como chave. " + dicionario["cor"])

# alterar valor
dicionario["cor"] = "branco"
print(dicionario["cor"])

# update()
dicionario.update({"ano": 2023})
print(dicionario)

# adicionar valores
dicionario["categoria"] = "sedã"
print(dicionario)
dicionario.update({"portas": 4})
print(dicionario)
dicionario.update({"sabor": 2.5})
print(dicionario)

# metodos e funções que se aplicam a coleções tambem podem se aplicar a dicionarios, veja na documentação
# remover item
dicionario.pop("sabor")
print(dicionario)

# remover todos os itens
dicionario2 = dicionario.copy()
print(dicionario2)
dicionario2.clear()
print(dicionario2)

# loops
for x in dicionario:
    print(x)  # chaves

print(".......................")

for x in dicionario.keys():
    print(x)  # chaves

print(".......................")

for y in dicionario:
    print(dicionario[y])

print(".......................")

for x in dicionario.values():
    print(x)

print(".......................")

for x in dicionario.items():
    print(x)

# copia
dicionario2 = dicionario.copy()
print(dicionario2)

dicionario3 = dict(dicionario2)  # outra forma
dicionario2.pop("cor")  # o valor continua pois foi feito uma copia anteriormente
print(dicionario3)

# diconarios encadeados
dicionario4 = {
    "aluno": {"nome": "Pedro", "idade": 15},
    "aluno2": {"nome": "Clara", "idade": 14},
    "aluno3": {"nome": "Ana", "idade": 16},
}
# dicionario encadeado
aluno4 = {"nome": "tião", "idade": 18}
dicionario5 = {"aluno4": aluno4, "dicionario4": dicionario4}
