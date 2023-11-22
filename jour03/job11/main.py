#méthode plus simple
def time_to_text(nombre):
    if nombre >= 60 :
        heure = nombre // 60
        minutes = nombre % 60
        print (heure,"heure",minutes,"minutes")
    else :
        print (nombre,"minutes")



time_to_text(68)
time_to_text(80)
time_to_text(30)
time_to_text(15)
time_to_text(1000)

#méthode plus compliqué pour rien mais rigolo
def time_to_text(nombre):
    test=0
    heure = -1
    while test < nombre :
        test += 60
        heure += 1
    
    minutes = 60 + (nombre - test)

    print(heure, "heure",minutes, "minutes")

time_to_text(1000)

#l'inverse de la méthode rigolo
def time_to_text(nombre):
    heure=0
    while nombre > 60 :
        nombre -= 60
        heure += 1

    print(heure, "heure",nombre, "minutes")

time_to_text(68)




