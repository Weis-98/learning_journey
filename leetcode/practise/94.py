# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        temp = []
        if root.left is not None:
            temp += self.inorderTraversal(root.left)
        temp += [root.val]
        if root.right is not None:
            temp += self.inorderTraversal(root.right)
        return temp