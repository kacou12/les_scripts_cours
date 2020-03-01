X = {"a","b","c","d"}
Y = {"s","b","d"}
print(X)
print(Y)
if "c"in X:
    print("c appartient")

if "a" in Y:
    print("a appartient")

X_Y= X-Y #suppression des elements repetitifs et garde reste du premier et pas du second
print(X_Y)
Y_X = Y-X
print(Y_X) #suppression des elements repetitifs et garde reste du second et pas du premier
X_U_F= X | Y
print(X_U_F) #garde les valeurs des 2 ensembles

X_n_F= X & Y
print(X_n_F) #garde les valeurs presentent dans les 2 ensembles
