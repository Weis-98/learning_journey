# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def maxmin(seed):
            root = seed            
            while root:
                Ml, Mr = -float('inf'), -float('inf')
                ml, mr = float('inf'), float('inf')
                if root.left is None:
                    # Ml, ml = root.val, root.val
                    bool1 = 1
                else:
                    Ml, ml, bool1 = maxmin(root.left)

                if root.right is None:
                    # Mr, mr = root.val, root.val
                    bool2 = 1
                else:
                    Mr, mr, bool2 = maxmin(root.right)

                if not bool1 or not bool2:
                    return -1, -1, 0
                if Ml >= root.val or mr <= root.val:
                    return -1, -1, 0
                else:
                    return max(Mr, root.val), min(ml, root.val), 1
        _, _, C = maxmin(root)
        return (C==1)