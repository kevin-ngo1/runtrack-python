for j in range (2,1001):
    for i in range (2,j) :
        if j % i == 0 :
            break
    else :
        print (j)

