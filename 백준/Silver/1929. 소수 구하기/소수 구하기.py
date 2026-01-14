import sys
import math
M, N = list(map(int, input().split()))
    
for i in range(M, N+1):
    if i == 1:
        continue
    
    for j in range(2, int(math.sqrt(i)) + 1): # 제곱근 확인
        if (i % j == 0):
            break
    
    else:
        print(i)
