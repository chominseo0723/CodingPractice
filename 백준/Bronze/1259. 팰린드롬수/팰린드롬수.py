import sys

while 1:
    word = input().strip()

    if word == "0":
        break

    elif word == word[::-1]:
        print("yes")

    else:
        print("no")