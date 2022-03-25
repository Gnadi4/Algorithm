# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([(root,1)])
        ans = 1
        while q:
            rt, cnt = q.popleft()
            if rt:
                if rt.left:
                    q.append((rt.left,cnt+1))
                    ans = max(ans, cnt+1)
                if rt.right:
                    q.append((rt.right,cnt+1))
                    ans = max(ans, cnt+1)
            else:
                ans = 0
                break
        return ans