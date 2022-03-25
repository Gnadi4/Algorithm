# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        def func(root):
            
            max_l = 0
            ans = 0
            b,c = 0,0
            if root.left:
                a,b = func(root.left)
                ans = max(ans, a)
            if root.right:
                a,c = func(root.right)
                ans = max(ans, a)
            ans = max(ans, b+c)
            max_l = max(b,c)
            return ans,max_l+1
        
        return func(root)[0]
        