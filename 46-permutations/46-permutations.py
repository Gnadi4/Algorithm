class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def func(count, s, ind):
            for i in range(len(nums)):
                if i not in ind:
                    if count<len(nums):
                        ind.append(i)
                        s.append(str(nums[i]))
                        func(count+1, s, ind)
                        s.pop()
                        ind.pop()
                    elif count==len(nums):
                        s.append(str(nums[i]))
                        ans.append(list(s))
                        s.pop()
            return
        
        func(1, [], [""])
        
        return ans