from collections import defaultdict as dd

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        comp_dict = dd(int)
        comp_val = 123
        ans = 0
        
        for i in jewels:
            comp_dict[ord(i)] = 1
        
        for i in stones:
            if comp_dict[ord(i)] == 1:
               ans +=1
        
        return ans