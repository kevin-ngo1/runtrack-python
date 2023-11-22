def what(type, saison):
    if type == "fruits" :
        if saison == "ete" :
            print ("Poire, fraise, cassis")
        elif saison == "hiver":
            print ("orange, mandarine et kiwi")
        else :
            print ("Tu as mal écrit la saison")
    elif type == "legume" :
        if saison == "ete" :
            print ("artichaut, aubergine,navet")
        elif saison == "hiver":
            print ("carotte, topinambour, endive")
        else :
            print ("Tu as mal écrit la saison")
    else :
        print ("Tu as mal écrit le type")

what("fruits", "oui")
what("non","ete")
what("fruits","ete")
what("legume","hiver")