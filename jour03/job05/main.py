def calcule(num1, operator, num2):
    if operator == "+" :
        return num1 + num2
    elif operator == "-" :
        return num1 - num2
    elif operator == "*" :
        return num1 * num2
    elif operator == "/" :
        return num1 / num2
    elif operator == "%" :
        return num1 % num2
    else :
        print("Le signe n'est pas correct")

print(calcule(5,"-",1))
print(calcule(5,"/",1))
print(calcule(5,"%",1))
print(calcule(5,"+",1))
print(calcule(5,"*",1))