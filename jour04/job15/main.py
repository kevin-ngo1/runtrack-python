def tri_arrondir(liste):

    taille=0
    i=0

    for nombre in liste :
        taille +=1

    for nombre in range(taille) :
        liste[nombre] = liste[nombre] - (liste[nombre] % 1)

    for i in range(taille):
        for j in range(i + 1, taille):
            if liste[j] < liste[i]:
                liste[i], liste[j] = liste[j], liste[i]

    print (liste)

tri_arrondir([22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50])