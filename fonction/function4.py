from math import pi,sqrt
a=(input("demi grand axe a = "))
b=(input("demi axe moyen b = "))
c=(input("demi petit axe c = "))
d=(input("densité d = "))

def volMasseEllipsoide(a=10,b=8,c=6,d=1):
    volume = float((4/3)*pi*a*b*c)
    e=sqrt((a**2-c**2)/a)
    masse=d*volume
    return e, volume, masse

try:
    a= float(a)
    b= float(b)
    c=float(c)
    d=float(d)
    if a>=b>=c:
        table=volMasseEllipsoide(a,b,c)
        print("l'enxentricité est : {:.4f}".format(table[0]))
        print("le volume est : {:.4f}".format(table[1]))
        print("la masse est : {:.4f}".format(table[2]),"kg")

    else:
        print("A doit etre superieur ou egal a B, qui doit etre superieur ou egal a C")
    
except :

    print("Veillez entrer des nombre")
