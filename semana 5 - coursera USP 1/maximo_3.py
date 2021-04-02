def maximo(x,y,z):
    if(z >= y and z >= x):
        return(z)
    elif(y >= z and y >= x):
        return(y)
    else:
        return(x)

print(maximo(16,15,-3))