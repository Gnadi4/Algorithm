class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        stp = 0
        tmp = {}
        for i in range(len(s)):
            if s[i] in tmp:
                if tmp[s[i]] + 1 > stp:
                    ans = max(i-stp, ans)
                    stp = tmp[s[i]] + 1
                tmp[s[i]] = i
            else:
                tmp[s[i]] = i
        ans = max(len(s)-stp, ans)
        return ans
    
'''
"abcabcbb"
"bbbbb"
"pwwkew"
"dvdf"
" "
""
"au"
"cdd"
"abba"
'''