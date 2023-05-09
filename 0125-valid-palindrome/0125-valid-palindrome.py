class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                tmp += i.lower()
        print(tmp)
        print(tmp[::-1])
        # if tmp == tmp[::-1]:
        #     return True
        # else:
        #     return False
        return tmp == tmp[::-1]