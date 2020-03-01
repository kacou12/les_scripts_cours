base=int(input("la base: "))
debut=int(input("la debut: "))
fin=int(input("la fin: "))
fin +=1
inc=int(input("la inc: "))


def yan(base, debut, fin, inc):
    for a in range(debut, fin, inc):
        print(base,"*",a,"=",base*a)


yan(base,debut,fin,inc)