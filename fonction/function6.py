def somme(n1,n2,n3):
    somme = n1+n2+n3
    return somme

tuple_var = []
longueur =len(tuple_var)
plus = 1
while longueur != 3:
   
    value=(input("Nombre : "))
    try:
        value= float(value)
        tuple_var.append(value)
        plus +=1
        longueur =len(tuple_var)

    except:
        print("Veillez ne pas entrer des chaines de caractères")
n0= tuple_var[0]
n1= tuple_var[1]
n2= tuple_var[2]
        
print(somme(n0,n1,n2))