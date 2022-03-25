# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        def func(root):
            max_l = 0
            ans = 0
            if not root:
                return 0
            if root.left:
                a,b = func(root.left)
                if a == root.val:
                    ans += b
                    max_l = max(max_l, b)
            if root.right:
                a,c = func(root.right)
                if a == root.val:
                    ans += c
                    max_l = max(max_l, c)
            self.longest = max(self.longest, ans)
            
            return root.val, max_l+1
        func(root)
        return self.longest