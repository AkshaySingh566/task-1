from array import *

arr = array('q', [])
print("enter the two nos.")
x = int(input("enter the 1st no."))
y = int(input("enter the 2nd no."))
i = 1
j = 1
c = 0
d = 0
print("The factors of 1st no. are")
while i <= x:
    s = x % i
    if s == 0:
        c += 1
        print(i)
        arr.append(i)
    i += 1
print()
print()
ar = array('b', [])
print("The factors of 2nd no. are")
while j <= y:
    t = y % j
    if t == 0:
        d = d + 1
        print(j)
        ar.append(j)
    j += 1
print()
print("The common factors are:")
for q in range(c):
    for b in range(d):
        if arr[q] == ar[b]:
            print(arr[q])


