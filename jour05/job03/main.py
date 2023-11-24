hauteur = int(input("Entrez la hauteur :"))

for i in range(hauteur):
    espaces = " "*(hauteur - i - 1)
    if i == hauteur - 1:
        print("/"+"_"*(2*i)+"\\")
    else:
        print(espaces+"/"+" "*(2 * i)+"\\")