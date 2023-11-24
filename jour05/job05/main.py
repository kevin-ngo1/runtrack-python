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

code("je suis maya the bee zzzzzz", -2)

