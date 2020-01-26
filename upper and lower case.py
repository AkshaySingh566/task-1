def case():
    word = input("Enter a word: ")

    up = 0
    low = 0
    length = len(word)

    for i in range(length):
        if word[i].isupper():
            up = up + 1
        elif word[i].islower():
            low = low + 1

    print("Uppercase letters: ", up)
    print("Lowercase letters: ", low)


case()