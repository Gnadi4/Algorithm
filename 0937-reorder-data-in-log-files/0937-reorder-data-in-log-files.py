class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        al, di = [], []
        for i in logs:
            if i.split()[1].isalpha():
                al.append(i)
            else:
                di.append(i)
        al.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return al+di