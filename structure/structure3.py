from itertools import product
mylist=[]
for x, y in product("abc", "de"):
    mot=x+y
    mylist.append(mot)
print(mylist[:])
