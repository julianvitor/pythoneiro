#-*- coding: utf-8 -*-
# python 3.10 

unidade = None 
match unidade:
    case "centímetro":
        print("distância")

    case "joule":
        print("trabalho")

    case "grama":
        print("massa")
    
    case "litro":
        print("volume")
    
    case _:
        print("nada")