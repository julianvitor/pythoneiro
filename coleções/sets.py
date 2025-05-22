# -*- coding: utf-8 -*-
# sets não possuem ordem, possuem itens imutaveis e não permitem itens duplicados mas voce pode adicionar novos itens ou remover
set1 = {"pé", "mão", "cabeça", "pé", "braço", "cerebro"}
print(set1)

# é possivel percorrer sets com loops apesar de não possuirem ordem
for x in set1:
    print(x)

# é possivel chegar a existencia de um item
print("pé" in set1)

# add
set1.add("braço")
print(set1)

# de um set para o outro
set2 = {"coração", "baço", "cerebro"}
set1.update(set2)
print(set1)

# discart ou remove (discard não depende da existencia do item)
set1.discard("coração")
set1.remove("baço")
print(set1)

# union
set3 = set1.union(set2)
print(set3)

# intersection
set3 = set1.intersection(set2)
print(set3)

# intersection_update
set1.intersection_update(set2)
print(set1)

# symetric_diference_update
set2 = {"coração", "baço", "cerebro"}
set1 = {"pé", "mão", "cabeça", "pé", "braço", "cerebro"}
set2.symmetric_difference_update(set1)
print(set2)
