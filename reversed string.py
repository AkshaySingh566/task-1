def rev():
    word = input("Enter a string: ")
    length = len(word)

    s = " "
    for i in reversed(range(length)):
        s = s + word[i]

    print("Reversed String is:", s)


rev()