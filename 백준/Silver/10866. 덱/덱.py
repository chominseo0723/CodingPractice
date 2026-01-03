import sys
input = sys.stdin.readline

X = int(input()) # 명령어 수 입력받음
commands = []
deque = []
for _ in range(X):
    commands = input().split() # 한줄로 읽어오고 나눔

    if (commands[0] == "push_front"):
        deque.insert(0, int(commands[1])) 
        
    elif (commands[0] == "push_back"):
        deque.append(int(commands[1]))
    elif (commands[0] == "pop_front"):
        if deque:
            print(deque.pop(0))
        else:
            print(-1)
    elif (commands[0] == "pop_back"):
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif (commands[0] == "size"):
        print(len(deque))       
    elif (commands[0] == "empty"):
        if len(deque) == 0:
            print(1)          # 비었으면 1
        else:
            print(0)          # 아니면 0
    elif (commands[0] == "front"):
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif (commands[0] == "back"):
        if deque:
            print(deque[-1])
        else:
            print(-1)