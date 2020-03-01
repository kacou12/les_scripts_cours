def somme(multi):
    longueur = len(multi)
    somme = 0
    for a in range(0,longueur):
        somme += multi[a]
    return somme

tuple_var = []
add = 0
while add != "n":
    add =input("voulez vous ajouter un nombre au tuple y/n:")
    if(add == "y"):
        value=(input("Nombre a jouter : "))
        print(type(value))
        try:
            value= float(value)
            tuple_var.append(value)
        except:
            print("Veillez ne pas entrer des chaines de caractères")

    else:
        print("Nous calculons la somme")
        break

print("La somme donne: ",somme(tuple_var))