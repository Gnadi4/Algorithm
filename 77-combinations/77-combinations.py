class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        li = [i for i in range(1,n+1)]
        
        def func(st, s):
            if len(s) == k:
                tmp = s.copy()
                ans.append(tmp)
                return
            for i in range(st, n):
                s.append(i+1)
                func(i+1, s)
                s.pop()
            return
        
        func(0, [])
        return ans