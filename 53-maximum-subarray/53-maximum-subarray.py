class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
#         def func(l,r):
            
#             if r-l <= 1:
#                 return nums[l]
            
#             res = max(func(l,(l+r)//2), func((l+r)//2,r))
            
#             left_b = nums[(l+r)//2]
#             left_sum = 0
#             for i in range((l+r)//2, l-1, -1):
#                 left_sum += nums[i]
#                 left_b = max(left_b, left_sum)
#             right_b = 0
#             right_sum = 0
#             for i in range(((l+r)//2)+1, r):
#                 right_sum += nums[i]
#                 right_b = max(right_b, right_sum)
                           
#             # print(res, right_b + left_b)
            
#             return max(res, right_b + left_b) 
        
#         return func(0, len(nums))
        dp = []
        for i in nums:
            if dp:
                dp.append(max(dp[-1]+i, i))
            else:
                dp.append(i)
                ans = dp[-1]
            ans = max(ans, dp[-1])
        return ans