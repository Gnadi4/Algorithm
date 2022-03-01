class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def func(su, st, val):
            if su>target:
                return
            elif su==target:
                tmp = sorted(val[:])
                if tmp not in ans: ans.append(tmp)
                return
            else:
                for i in range(st, len(candidates)):
                    val.append(candidates[i])
                    func(su+candidates[i], i, val)
                    val.pop()
            return
        
        func(0, 0, [])
        
        return ans