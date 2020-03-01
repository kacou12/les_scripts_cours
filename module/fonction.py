from math import sqrt

def maFonction(a,b,c):
    delta=b**2-(4*a*c)
    if(delta > 0):
        x=(-b-sqrt(delta))/2
        y=(-b+sqrt(delta))/2
        finish= (2,x,y)
        return finish
    elif (delta == 0):
        x=(-b/(2*a))
        finish= (1,x,0)
        return finish
    else:
        finish= (0,0,0)
        return finish