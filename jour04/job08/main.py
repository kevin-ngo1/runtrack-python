L = [8,24,27,8,2,16,9,7,84,91]
res=0

for nombre in L:
    if nombre % 2 == 0 :
        res += nombre

print ("La somme des pairs est",res)