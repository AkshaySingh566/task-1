def dup():
    word = input("Enter a word: ")
    length = len(word)

    s = " "
    for i in range(length):
        for j in range(i+1):
            if word[i] == word[j]:
                break
        if j == i:
            s = s + word[i]
            print(s, end=" ")

    print("Word after removing duplicate characters is: ", s)


dup()