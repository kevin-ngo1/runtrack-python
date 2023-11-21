nom = "Figurine Jujutsu Kaisen - Gojo"
prix_unitaire = 35
quantité_en_stock = 16

print("Produit :",nom)
print("Prix :",prix_unitaire)
print("Quantité :",quantité_en_stock)

ajout = int(input("Entrez la quantité de produits à àjouter au stock :"))
quantité_en_stock += ajout

prix_unitaire *= 1.10

print("Produit :",nom)
print("Prix :",prix_unitaire)
print("Quantité :",quantité_en_stock)



