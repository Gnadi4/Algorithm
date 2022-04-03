# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        q = [root]
        while q:
            r = q.pop()
            if r.right: 
                q.append(r.right)
            if r.left:
                q.append(r.left)
            r.left, r.right = r.right, r.left
        return root
                