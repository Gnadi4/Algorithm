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
        
        if len(digits)>=1:
            for i in let[digits[0]]:
                if len(digits)>=2:
                    for j in let[digits[1]]:
                        if len(digits)>=3:
                            for l in let[digits[2]]:
                                if len(digits)>=4:
                                    for m in let[digits[3]]:
                                        ans.append(i+j+l+m)
                                else:
                                    ans.append(i+j+l)
                        else:
                            ans.append(i+j)
                else:
                    ans.append(i)
            
        return ans