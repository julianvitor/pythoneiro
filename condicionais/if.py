# -*- coding: utf-8 -*-

x = int(input("x: "))
y = int(input("y: "))
if y > x:
    print("y maior que x")
elif x == y:
    print("x e y são iguais") 
else :
    print("x maior que y")

#encurtamento if else
print("----------encurtamento----------")
x,y = int(input("x: ")), int(input("y: "))
print("x > y") if x > y else print ("=") if x==y else print("y > x") #if dentro do else

#and
print ("---------and----------")
a,b,c = int(input("a: ")), int(input("b: ")), int(input("c: "))
if a > b and c > a:
    print("c é maior que b")

#or
print ("---------or----------")
a,b,c = int(input("a: ")), int(input("b: ")), int(input("c: "))
if b > a or c > a:
    print("alguem é maior que A")

#instrução pass 
if 5>1:
    pass