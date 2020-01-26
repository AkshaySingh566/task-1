print("select the no. of lines")
x=int(input())
i=1
l=1
while i<=x:
    j=1
    while j<=2*x:
        if (x-l)<j<(x+l):
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    i+=1
    l+=1
    print()
