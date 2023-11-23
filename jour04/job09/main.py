L = [8,24,27,48,2,16,9,102,7,84,91]
maxi =L[0]
mini =L[0]

for nombre in L :
    if maxi < nombre :
        maxi = nombre

for nombre in L :
    if mini > nombre :
        mini = nombre
    
print("La valeur max est :",maxi, "\nLa valeur minimum est :",mini)
