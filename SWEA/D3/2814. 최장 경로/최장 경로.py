from collections import defaultdict
import heapq

t = int(input())

for test in range(1,t+1):
    n,m = map(int, input().split())
    
    dict_co = defaultdict(list)
    q = []
    for i in range(m):
        a,b = map(int, input().split())
        dict_co[a].append(b)
        dict_co[b].append(a)
        heapq.heappush(q, (1, a, []))
        heapq.heappush(q, (1, b, []))
    # chk = []
    ans = 1
    while q:
        num, st, chk = heapq.heappop(q)
        if st not in chk:
            chk.append(st)
            for i in dict_co[st]:
                if (i not in chk):
                    heapq.heappush(q, (num+1, i, chk))
                    ans = max(ans, num+1)
    
    print("#{} {}".format(test, ans))