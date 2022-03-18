from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dict_co = defaultdict(list)
        
        for x,y in prerequisites:
            dict_co[x].append(y)
        visited = set()
        bef_chk = set()
        def func(val):
            if val in bef_chk: return False
            if val in visited: return True
            bef_chk.add(val)
            for i in dict_co[val]:
                if not func(i): return False
            
            bef_chk.remove(val)
            visited.add(val)
            return True
        
        for i in list(dict_co):
            if not func(i): return False
        return True
        