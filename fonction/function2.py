from math import pi
nombre= int(input("entrer un nombre: "))
def cube(nombre):
    print(nombre**3)
    val= nombre**3
    return val

cube(nombre)

rayon = int(input("entrer un rayon: "))
def volumeSphere(r):
    result = (4*pi*r)/3
    print(result)

volumeSphere(cube(nombre))