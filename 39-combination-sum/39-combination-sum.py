class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def func(val):
            sum_val = sum(val)
            if sum_val>target:
                return
            elif sum_val==target:
                tmp = sorted(val[:])
                if tmp not in ans: ans.append(tmp)
                return
            else:
                for i in candidates:
                    val.append(i)
                    func(val)
                    val.pop()
            return
        
        func([])
        
        return ans