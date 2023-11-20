#méthode compréhensible :

debut = ord("a")
fin = debut + 26

print("Méthode compréhensible :")
while debut < fin :
    print(chr(debut), end=" ")
    debut += 1

#méthode simplifiée :

print("Méthode simplifiée :")
for letter in range(97, 123):
    print(chr(letter), end=" ")