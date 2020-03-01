dico={
    "dic1":{"un":1,"deux":2,"trois":3},
    "dic2":{"dix":10,"quatre":4,"cinq":5},
    "dic3":{"six":6,"sept":7,"huit":8},
    "dic4":{"neuf":9,"onze":11,"douze":12}
}
def dictionnary(dico):
    for cle in dico:
        for cle_second, second_val in dico[cle].items():
            print(cle_second,":", second_val)
    
dictionnary(dico)