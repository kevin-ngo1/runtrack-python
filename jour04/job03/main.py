#sans return
def liste_ajout():
    liste = ["pomme","cerise","orange"]
    liste.append("Melon")
    print (liste)

liste_ajout()

#avec return
def liste_ajout():
    liste = ["pomme","cerise","orange"]
    liste.append("Melon")
    return liste

print(liste_ajout())

