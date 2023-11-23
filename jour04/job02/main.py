#sans return
def liste():  
    fruits = ["pomme","cerise","orange"]
    print (fruits[1])

liste()

#avec return
def liste():  
    fruits = ["pomme","cerise","orange"]
    return (fruits[1])

print(liste())