def fabonaci(n):
    n1=1
    n2=1
    n3=1
#123123
    if(n<1):
        return -1
    while(n-2)>0:
        n3=n1+n2
        n1=n2
        n2=n3

        n=n-1

    return n3

sum=fabonaci(20)
print (sum)