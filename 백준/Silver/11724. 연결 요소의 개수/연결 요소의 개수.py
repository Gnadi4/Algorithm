import sys
from collections import defaultdict
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m = map(int, input().rstrip().split())
visited = [0]*(n+1)
visited[0] = 1
graph = defaultdict(list)
for i in range(m):
    a,b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

def func(s):
    visited[s] = 1

    for i in graph[s]:
        if visited[i]==0:
            func(i)

    return

ans = 0
for i in range(n+1):
    if visited[i]==0:
        func(i)
        ans+=1

print(ans)