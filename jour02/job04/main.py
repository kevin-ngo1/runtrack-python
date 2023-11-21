nombre = int(input("Saisir un nombre :"))

if nombre < 0 :
    print("Veuillez saisir un nombre étant un éntier supérieur à zéro")
else :
    for n in range (1,nombre+1) :
        print ("Table de Multiplication :",n)
        for i in range (1,11) :
            print(i, "x",n, "=", i * n )

