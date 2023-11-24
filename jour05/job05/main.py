#sans input
def code(message, decale):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    res=""
    tmp = 0
    for lettre in message :
        for j in range(len(alphabet)) :
            if lettre == alphabet[j] :
                if j+decale > 25 :
                    tmp = j+decale - 26
                    res += alphabet[tmp]
                else :
                    res += alphabet[j+decale]
    print(res)

code("je suis maya the bee zzzzzzyyyzzzz", 2)

#avec input
def code(message, decale):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    res=""
    tmp = 0
    for lettre in message :
        for j in range(len(alphabet)) :
            if lettre == alphabet[j] :
                if j+decale > 25 :
                    tmp = j+decale - 26
                    res += alphabet[tmp]
                else :
                    res += alphabet[j+decale]
    print(res)

message = input("Entrez votre message qui sera chiffré (tout en minuscule) :")
decale = int(input("Entrez le nombre de décalage :"))
code(message, decale)

