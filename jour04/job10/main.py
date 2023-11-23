L = [8,24,27,48,2,16,9,102,7,84,91]
res = 1

for nombre in L :
    if nombre >=25 and nombre <= 90 :
        res *= nombre

print("Le produit des nombres entre 25 et 90 est",res)
