chaine1=str(input("chaine 1: "))
chaine2=str(input("chaine2: "))
if len(chaine1) > len(chaine2):
    print(chaine2)
elif  len(chaine1) < len(chaine2):
    print(chaine1)
else:
    print("Egalité")