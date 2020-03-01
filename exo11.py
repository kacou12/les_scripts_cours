from math import sin

for a in range(-3,4):
    try:
        print(sin(a)/a)
    except:
        print("Trop d'erreurs")
    
    