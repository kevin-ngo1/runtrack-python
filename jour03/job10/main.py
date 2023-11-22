def pair_impair(n):
    if n >= 0 :
        print ("Entier positif")
        if n % 2 == 0 :
            print("Pair")
        else :
            print("Impair")
    else :
        print ("C'est un entier négatif !")
    

pair_impair(6)
pair_impair(2)
pair_impair(3)
pair_impair(-5)

