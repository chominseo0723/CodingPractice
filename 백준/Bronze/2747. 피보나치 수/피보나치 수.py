import sys;

N = int(input())

dp = [0] * (N+1) # 리스트 N+1 개 복사 dp=[0,0,0,0,0,0,,,...]

if N >= 1:
    dp[1] = 1

for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N]) # N번째 값 print