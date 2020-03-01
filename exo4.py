pSeuil=2.3
vSeuil=7.41
pression=int(input("Entrez la pression : "))
volume=int(input("Entrez le volume: "))
if pression > pSeuil and  volume > vSeuil:
    print("Arret immediat")
elif pression > pSeuil and  volume <= vSeuil:
    print("demander d'augmenter le volume de l'enceinte")
elif pression <= pSeuil and  volume > vSeuil:
    print("Demander de diminuer le volume de l'enceinte")
else:
    print("Tout va bien")