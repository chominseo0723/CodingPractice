import sys
N = int(input())

schedule = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

# dp[i] : i번째 날까지 얻을 수 있는 최대 수익
dp = [0 for i in range(N+1)]


# i 번재 날에 상담을 시작한다 가정
for i in range(N):
   # 상담 안 하는 경우 (다음 날로 수익 넘김), 상담을 안해도 날짜 인덱스 하나 더 증가 시켜줌
    dp[i + 1] = max(dp[i + 1], dp[i])

    #  t : i번째 날에 시작하는 상담 기간, p : 그 상담 했을때 받는 돈
    t, p = schedule[i]

    # i+t : 상담 끝난날
    if i + t <= N:
        dp[i + t] = max(dp[i + t], dp[i] + p)

print(dp[N])