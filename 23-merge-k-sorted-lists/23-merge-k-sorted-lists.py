# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = []
        for l in lists:
            while l:
                ans.append(l.val)
                l = l.next
        ans.sort()
        ret = res = ListNode()
        for i in range(0,len(ans)):
            tmp = ListNode(ans[i])
            res.next = tmp
            res = res.next
            
        return ret.next