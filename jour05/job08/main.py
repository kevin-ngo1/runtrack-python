def my_sort(liste):
    coups = 0
    for i in range(len(liste)):
        for j in range(0, len(liste)-i-1):
            if liste[j+1] < liste[j]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
                coups +=1
    print("Nombre total de coups nécessaires pour trier la liste :",coups,"\nListe triée :",liste)

my_sort([4,8,6,7,2,1,3,9,5])
    
