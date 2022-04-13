import sys
input = sys.stdin.readline
from collections import deque
import heapq

n = int(input().rstrip())
q = []
for _ in range(n):
    a = int(input().rstrip())
    if a == 0:
        if q:
            print(-1*heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q,-1*a)