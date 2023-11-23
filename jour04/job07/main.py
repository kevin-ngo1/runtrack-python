L=[8,24,48,2,16]
i=0

for nombre in L :
    if nombre % 3 == 0 :
        i += 1
    
print("Le nombre de multiple de 3 dans la liste est",i)