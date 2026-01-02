N = int(input())

numbers = []

for _ in range(N):
    num = int(input()) # 각 줄마다 숫자 하나씩 입력받기
    if(num == 0):
        numbers.pop()
    else:
        numbers.append(num)
print(sum(numbers))
