import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        tmp = {}
        heap = []
        for i in nums:
            if i in tmp:
                tmp[i] += 1
            else:
                tmp[i] = 1
        # print(tmp)
        for i in tmp:
            heapq.heappush(heap, (tmp[i], i))
        for i in range(len(tmp)-k):
            heapq.heappop(heap)
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
    
    
'''
[1,1,1,2,2,3]
2
[1]
1
[1,2]
2
'''