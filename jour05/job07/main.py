def luke(notes):
    notes_arrondi=[]
    for nombre in notes :
        if nombre % 5 in [3,4] :
            res = round(nombre / 5) * 5
            notes_arrondi += [res]
        else :
            notes_arrondi += [nombre]
    print (notes_arrondi)


luke([12,88,83,82,10,13,18])
