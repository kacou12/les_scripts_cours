from math import sqrt
nombre = float(input("Nombre flottant: "))
nombre = int(nombre)
if nombre > 0 or nombre == 0 :
    print(sqrt(nombre)) 
else:
    print("erreur")