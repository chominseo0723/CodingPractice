import sys

# 한 번 있었던 문자가 다음에 또 등장하면 안됨
N = int(input())
result = N

for i in range(N):
    word = input() # 단어 하나 입력받기
    
    for j in range(len(word)-1):
        if word[j] == word[j+1]: # 이게 다르면 연속이 끊김
            pass
        elif word[j] in word[j+1:]: # j+1 부터 끝까지
            result -= 1
            break

print(result)
