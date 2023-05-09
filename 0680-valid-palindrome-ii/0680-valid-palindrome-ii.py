class Solution:
    def validPalindrome(self, s: str) -> bool:
        s_tmp = s[::-1]
        if s == s_tmp: return True
        for i in range(len(s)):
            if s[i] != s_tmp[i]:
                
                s_tmp1 = s_tmp[0:i] + s_tmp[i+1:]
                s1 = s_tmp1[::-1]
            
                s2 = s[0:i] + s[i+1:]
                s_tmp2 = s2[::-1]

                return (s1 == s_tmp1 or s2 == s_tmp2)
                