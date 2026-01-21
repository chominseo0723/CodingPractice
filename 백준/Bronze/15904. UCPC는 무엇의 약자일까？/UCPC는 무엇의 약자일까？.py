word = input()
include = list("UCPC") # 비교 할 문자
correct = []

index = 0

for i in word:
    if index < len(include) and i == include[index]:
        correct.append(i)
        index += 1

if correct == list(include):
    print("I love UCPC")
else:
    print("I hate UCPC")