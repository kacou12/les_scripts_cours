from math import sqrt
from fonction import *

a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))

resultat = maFonction(a,b,c) 
if resultat[0] == 0:
    print("il n'y a pas de solutions")
elif resultat[0] == 1:
    print("il existe 1 solution unique x =", resultat[1])
elif resultat[0] == 2:
    print("il existe 2 solutions x =", resultat[1],"et y =", resultat[2])
