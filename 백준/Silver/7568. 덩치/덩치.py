import sys

N = int(input())
member = []
rank = [] # 등수

for _ in range(N): # 리스트로 저장
    weight, height = map(int, input().split()) # 몸무게 , 키 입력
    member.append((weight, height))

# print(member) 

for i in range(N):
    cnt = 1 # 가장 큰 등수를 1로 시작
    for j in range(N): # 모든 사람과 비교
        if i == j:
            continue
        if (member[j][0] > member[i][0] and member[j][1] > member[i][1]):
            cnt += 1
    rank.append(cnt) 

print(*rank)