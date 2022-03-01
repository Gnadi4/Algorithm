class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        let = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"],
        }
        
        ans = []
        
        def func(ind,s):
            for i in let[digits[ind]]:
                if len(s)+1<len(digits): func(ind+1,s+i)
                elif len(s)+1==len(digits): 
                    ans.append(s+i) 
            return
        if len(digits)==0: return ans
        func(0,"")
        return ans