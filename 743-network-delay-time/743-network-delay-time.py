from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dict_co = defaultdict(list)
        for i in times:
            dict_co[i[0]].append((i[1], i[2]))
        
        q = []
        dist = defaultdict(int)
        prev = defaultdict(int)
        for i in range(1,n+1):
            dist[i] = float('inf')
            prev[i] = None
            heapq.heappush(q, (dist[i], i))
        dist[k] = 0
        chk = True
        while q:
            l = len(q)
            tmp = []
            for _ in range(l):
                tmp.append(heapq.heappop(q))
            for i in tmp:    
                heapq.heappush(q, (dist[i[1]], i[1]))
            list_u = heapq.heappop(q)
            for i in dict_co[list_u[1]]:
                alt = dist[list_u[1]] + i[1]
                print(alt)
                if alt < dist[i[0]]:
                    dist[i[0]] = alt
                    prev[i[0]] = list_u[1]
        ans = []
        for i in dist:
            if dist[i] == float('inf'):
                chk = False
                break
            ans.append(dist[i])
        
        if chk:
            return max(ans)
        else:
            return -1
            
                    
                