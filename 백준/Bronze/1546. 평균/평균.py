import sys

N = int(input())
score = list(map(int, input().split())) # N 만큼 입력받기
max_score = max(score) #배열 안에서 최댓값
X = max_score / 100

result = sum(score) / X / N

print(result)
