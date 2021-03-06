# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def same(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 and root2 and root1.val == root2.val:
            return self.same(root1.left, root2.right) and self.same(root1.right, root2.left)
        else:
            return False

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.same(root, root)