# -*- coding: utf-8 -*-
a = 0 
while a != 10:
    print(a)
    a = a+1
    if a > 4:
        break
print("---------------")

b = 0
while b < 6:
    b += 1
    if b == 3:
        continue
    print(b)
print("---------------")

c = 0 
print(c)
while c < 10:
    c += 1
    print(c)
else:
    print("c não é menor que 10 agora")

