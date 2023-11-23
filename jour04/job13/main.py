#sans fonction
liste = [10,20,30,20,10,50,60,40,80,50,40]
liste_sans_doublon=[]

taille=0

for nombre in liste :
        taille +=1

for i in range(taille):
    for j in range(i + 1, taille):
        if liste[i] == liste[j] :
            break
    else :
        liste_sans_doublon = liste_sans_doublon + [liste[i]]
        

print (liste_sans_doublon)

#avec une fonction
def doublon(liste):

    liste_sans_doublon=[]

    taille=0

    for nombre in liste :
            taille +=1

    for i in range(taille):
        for j in range(i + 1, taille):
            if liste[i] == liste[j] :
                break
        else :
            liste_sans_doublon = liste_sans_doublon + [liste[i]]

    print(liste_sans_doublon)

doublon([10,20,30,20,10,50,60,40,80,50,40])

