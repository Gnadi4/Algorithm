import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int, input().rstrip().split())

list_n = deque([])
for _ in range(n):
    list_n.appendleft(int(input().rstrip()))

ans = 0
for i in list_n:
    ans += (k//i)
    k%=i
    if k==0: break

print(ans)