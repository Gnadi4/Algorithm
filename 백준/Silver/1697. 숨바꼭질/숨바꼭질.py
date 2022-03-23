import sys
from collections import deque, defaultdict
input = sys.stdin.readline
n,k = map(int, input().rstrip().split())

if n>=k: print(n-k)
else:
    q = deque([(n,0)])
    visited = defaultdict(int)
    while q:
        val = q.popleft()
        if val[0]==k: 
            print(val[1])
            break
        elif val[0]<k:
            if not visited[val[0]]:
                visited[val[0]]=val[1]
                q.append((val[0]+1, val[1]+1))
                q.append((val[0]-1, val[1]+1))
                q.append((val[0]*2, val[1]+1))
        else:
            if not visited[val[0]]:
                visited[val[0]]=val[1]
                q.append((val[0]-1, val[1]+1))
