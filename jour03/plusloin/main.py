#méthode super simple mais vraiment hyper simple
def inverse(mot):
    return mot[::-1]

print(inverse("oui"))
print(inverse("non"))
print(inverse("kayak"))
print(inverse("SKTT1"))
print(inverse("Worlds2023"))
print(inverse("nikana"))

#méthode compliqué pour s'amuser
def inverse(mot):
    mot_inverse=""
    for i in range (len(mot) -1, -1, -1) :
        mot_inverse += mot[i]
    print(mot_inverse)

print(inverse("oui"))
print(inverse("non"))
print(inverse("kayak"))
print(inverse("SKTT1"))
print(inverse("Worlds2023"))
print(inverse("nikana"))