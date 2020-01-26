print("Choose the no.")
x=int(input())
i=2
k=0
if x<3:
    if x<2:
        print("It is not a prime no.")
    else:
        print("It is prime no.")
else:
    while i<x:
        j=x%i
        if j==0:
            k+=1
        i=i+1
    if k==0:
        print("It is prime no.")
    else:
        print("It is not a prime no.")
