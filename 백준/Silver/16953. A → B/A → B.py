import sys
import heapq
input = sys.stdin.readline

n,m = map(int, input().rstrip().split())

q = []
heapq.heappush(q, (1,n))
ans = -1
while q:
    val = heapq.heappop(q)
    if val[1] == m:
        ans = val[0]
        break
    elif val[1] < m:
        heapq.heappush(q, (val[0]+1, val[1]*2))
        heapq.heappush(q, (val[0]+1, val[1]*10+1))
print(ans)