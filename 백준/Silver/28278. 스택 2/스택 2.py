# 스택은 int 만 들어감
import sys
input = sys.stdin.readline

N = int(input()) # 명령어 수
stack = []

for _ in range(N):
    cmd = input().split()
    num = int(cmd[0]) # 명령어 번호

    if (num == 1):
        stack.append(int(cmd[1])) # X push

    elif (num == 2):
        if stack:
            print(stack.pop())
        else: 
            print(-1)

    elif num == 3:
            print(len(stack))

    elif num == 4:
            if len(stack) == 0:
                print(1)          # 비었으면 1
            else:
                print(0)          # 아니면 0

    elif num == 5:
            if stack:
                print(stack[-1])
            else:
                print(-1)