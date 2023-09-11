import sys

input = sys.stdin.readline

l = list(map(int, input().rstrip().split()))
ans = [1,1,2,2,2,8]

for i in range(len(l)):
    print(ans[i] - l[i], end = ' ')