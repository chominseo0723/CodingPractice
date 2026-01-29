import sys

# 괄호 -> 스택

T = int(input()) # T개

for _ in range(T):
    cnt = 0  # 현재 열려 있는 '(' 괄호의 개수
    Valid = True
    word = input().strip()

    for i in word:
        if i == '(':
            cnt += 1
        else: 
            cnt -= 1
            # 닫는 괄호가 더 많아지는 순간 올바른 괄호 문자열 절대 X
            if cnt < 0: # ) 괄호가 더 많아짐
                Valid = False
                break
    if cnt != 0:
        Valid = False

    print("YES" if Valid else "NO")