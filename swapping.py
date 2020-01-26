def swap():
    a = int(input("Enter first number"))
    b = int(input("Enter another number"))

    print("Before Swapping:")
    print("a = ", a, " b = ", b)
    a = a+b
    b = a-b
    a = a-b
    print("After Swapping:")
    print("a = ", a, " b = ", b)


swap()