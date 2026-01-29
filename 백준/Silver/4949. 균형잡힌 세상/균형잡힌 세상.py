import sys

while 1:
    word = input() # 문자열 입력받기

    if word == ".":
        break

    box = [] # 괄호만 담을 리스트
    for i in word:
        if i in "()[]": # 문제에서 주어진 문자가 문자가 있다면 담음
            box.append(i)

    result = "".join(box) # 담은 문자들을 합침 (리스트 -> 문자열로 변환)

    while 1:
        if result == "": # 빈 문자열이라면 yes
            print("yes")
            break
        elif "()" not in result and "[]" not in result:
            print("no") # [] or () 가 없다면 no 출력
            break
        else: # 발견되는 () or [] 제거
            result = result.replace("()", "") 
            result = result.replace("[]", "")