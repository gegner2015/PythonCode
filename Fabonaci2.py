def Fabonaci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return Fabonaci(n-1)+Fabonaci(n-2)

print(Fabonaci(25))
