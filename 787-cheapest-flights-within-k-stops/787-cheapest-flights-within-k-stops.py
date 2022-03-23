from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dd = defaultdict(list)
        visited = defaultdict(list)
        for i,j,lim in flights:
            dd[i].append((j,lim))
        q = [(0,src,0)]
        while q:
            # print(q)
            i,j,lim = heapq.heappop(q)
            
            if lim in visited[j]:
                continue
            visited[j].append(lim)
            
            if j == dst: 
                return i
            if lim <= k:
                for d,p in dd[j]:
                    alt = i+p
                    heapq.heappush(q,(alt,d,lim+1))                           
        return -1