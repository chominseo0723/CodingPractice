import sys

line = list(map(int, input().split()))

N = line[0] # N명의 사람
K = line[1] # 양의 정수K

box = [] # 저장할 박스를 만든다.
result = []

for i in range(1, N+1):
    box.append(i)
# box = [1, 2, 3, ..., N]

idx = 0

while box: # box가 비어 있지 않은 동안 반복
    idx = (idx + K-1) % len(box)
    result.append(box.pop(idx))

print("<"+", ".join(map(str, result))+">")