class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        
        def func(ind, s):
            for i in range(ind, len(nums)):
                s.append(nums[i])
                ans.append(s.copy())
                func(i+1, s)
                s.pop()
            return
        
        func(0, [])
        
        return(ans)