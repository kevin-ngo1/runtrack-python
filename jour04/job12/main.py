def tri_croissant(liste):

    taille=0
    i=0

    for nombre in liste :
        taille +=1

    for i in range(taille):
        for j in range(i + 1, taille):
            if liste[j] < liste[i]:
                liste[i], liste[j] = liste[j], liste[i]

    print (liste)

tri_croissant([4,19,40,3,7,30,2,1])

 


