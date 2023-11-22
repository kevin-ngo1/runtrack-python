def time_to_text(nombre):
    if nombre >= 60 :
        heure = nombre // 60
        minutes = nombre % 60
        print (heure,"heure",minutes,"minutes")
    else :
        print (nombre,"minutes")



time_to_text(69)
time_to_text(80)
time_to_text(30)
time_to_text(15)
time_to_text(1000)