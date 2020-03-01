

from math import sqrt
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))


def maFonction(a,b,c):
    delta=b**2-(4*a*c)
    if(delta > 0):
        x=(-b-sqrt(delta))/2
        y=(-b+sqrt(delta))/2
        print("les solutions sont x =",x,"et y =", y)

    elif (delta == 0):
        x=int(-b/(2*a))
        print("la solution est",x)
    else:
        print("pas de solution")

maFonction(a,b,c) 
