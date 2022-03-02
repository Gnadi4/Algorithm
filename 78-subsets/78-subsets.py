class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def func(ind, s):
            ans.append(s)
            
            for i in range(ind, len(nums)):
                func(i+1, s + [nums[i]])
            return
        
        func(0, [])
        
        return(ans)