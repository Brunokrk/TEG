niveis = {
        '0':[1, 2, 3], #nivel zero
        '1':[4, 5], #nivel um
    }

m = niveis.values()
#print(niveis.values())
print(len(niveis))
for key in niveis:
    for value in niveis[key]:
        print(value)