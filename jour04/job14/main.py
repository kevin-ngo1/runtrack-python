def my_long_word(nombre, chaine):
    mot = ''
    res = ''
    longueur = 0 

    for caractere in chaine:
        if caractere != ' ':
            mot += caractere
            longueur += 1 
        else:
            if longueur > nombre:
                res += mot + ' '
            mot = ''
            longueur = 0 
    
    if longueur > nombre:
        res += mot
    
    return res

print(my_long_word(3,"La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"))