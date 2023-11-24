def phare(nombre, hauteur):
    metre = ((2*(nombre * hauteur)) / 100) * 5
    distance = metre * 7 

    print("Pour",nombre,"marches de",hauteur,"cm, le gardien parcourt",distance,"m par semaine")

phare(65, 25)


