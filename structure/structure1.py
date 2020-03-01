my_list=[17, 38, 10, 25, 72]
#1 trie et affiche list

my_list.sort()
print("liste triée:",my_list[:])

#2 add 12 et afficj=he list
my_list.append(12)
print("liste triée:",my_list[:])

#3 renverser et afficher list
my_list.reverse()
print("liste :",my_list[:])

#4 affichez l’indice de l’élément 17
index = my_list.index(17)
print("l'index de 17 est :",index)

#5 enlevez l’élément 38 et affichez la liste 
index = my_list.index(38)
my_list.pop(index)
print("liste pres suppression de l'element 38 :",my_list[:])

#6 affichez la sous-liste du 2eme 3eme élément ;
sous_list = my_list[1:3]
print("sous-liste du 2eme 3eme élément",sous_list[:])

#7 affichez la sous-liste du début au 2eme élément ;
sous_list = my_list[:2]
print("sous-liste du début au 2eme élément",sous_list[:])

#8 affichez la sous-liste du 3eélément à la fin de la liste ;
sous_list = my_list[2:]
print("sous-liste du 3eélément à la fin de la liste",sous_list[:])

#9 affichez le dernier élément en utilisant un indiçage négatif.
sous_list = my_list[-1:]
print("dernier élément en utilisant un indiçage négatif",sous_list)




