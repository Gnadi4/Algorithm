import sys
input = sys.stdin.readline

n = int(input().rstrip())

dp = [(1,0),(0,1)]

for i in range(2,41):
    dp.append((dp[i-1][0]+dp[i-2][0],dp[i-1][1]+dp[i-2][1]))

for _ in range(n):
    a = int(input().rstrip())
    print(dp[a][0],dp[a][1])
