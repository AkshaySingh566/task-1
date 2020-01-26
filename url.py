import re


def find():
    string = input("Enter a string: ")
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]| [! * \(\),] | (?: %[0-9a-fA-F][0-9a-fA-F]))+', string)
    print("URL is: ", url)


find()
