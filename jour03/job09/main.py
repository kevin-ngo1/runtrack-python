def moyenne(note1,note2,note3):
    moyenne_etudiant =round((note1 + note2 + note3)/3)

    if moyenne_etudiant >= 15 and moyenne_etudiant <= 20 :
        print ("Très bon élève")
    elif moyenne_etudiant >= 11 and moyenne_etudiant <= 14 :
        print ("Bon élève")
    elif moyenne_etudiant >= 8 and moyenne_etudiant <= 10 :
        print ("Élève moyen")
    elif moyenne_etudiant >= 0 and moyenne_etudiant <= 7 :
        print ("Élève devant faire des efforts")
    else :
        print ("Vous avez fait un erreur sur une note")
    
    return moyenne_etudiant

note1=float(input("Entrez votre première note :"))
note2=float(input("Entrez votre deuxième note :"))
note3=float(input("Entrez la dernière note :"))

print("La moyenne de l'élève est de", moyenne(note1, note2, note3))







