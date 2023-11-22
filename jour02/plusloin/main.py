a = int(input("Entrez la longueur du coté a :"))
b = int(input("Entrez la longueur du coté a :"))
c = int(input("Entrez la longueur du coté a :"))

if a == b and b == c :
    print ("C'est un triangle équilatéral")
elif a == b or b == c or a == c :
    if a**2+b**2 == c**2 or b**2+c**2 == a**2 or c**2+a**2 == b**2:
        print ("C'est un triangle rectangle et isocèle")
    else :
        print ("C'est un triangle isocèle")
elif a**2+b**2 == c**2 or b**2+c**2 == a**2 or c**2+a**2 == b**2:
    print ("C'est un triangle rectangle")
else :
    print ("C'est un triangle quelconque")
