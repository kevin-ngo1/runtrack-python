#méthode compréhensible :

debut = ord("z")
fin = ord("a") - 1 

print("Méthode compréhensible :")
while debut > fin:
    print(chr(debut), end=" ")
    debut -= 1


#méthode simplfiée :

print("Méthode simplifiée :")
for letter in range(122, 96, -1):
    print(chr(letter), end=" ")