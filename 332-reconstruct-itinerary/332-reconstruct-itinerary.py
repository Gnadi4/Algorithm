from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ans = ["JFK"]
        dict_t = defaultdict(list)
        for i in tickets:
            dict_t[i[0]].append(i[1])
        
        for i in dict_t:
            dict_t[i].sort()
        
        def func(st, dict_tmp):
            for i in range(len(dict_tmp[st])):
                if dict_tmp[st][i] != "":
                    ans.append(dict_tmp[st][i])
                    dict_tmp[st][i] = ""
                    if func(ans[-1], dict_tmp):
                        return True
                    dict_tmp[st][i] = ans.pop()
            
            for i in dict_tmp:
                for j in dict_tmp[i]:
                    if j!="":
                        return False
            return True
            
        func(ans[0], dict_t)
            
        return ans
        