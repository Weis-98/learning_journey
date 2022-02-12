# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res = 10**5
        self.pre = -10 ** 5

    def minDiffInBST(self, root: TreeNode) -> int:
        if root == None:
            return None

        def dfs(root: TreeNode):
            if root != None:
                dfs(root.left)
                self.res = min(self.res, root.val - self.pre)
                self.pre = root.val
                dfs(root.right)

        dfs(root)
        return self.res

node0 = TreeNode(0)
node12 = TreeNode(12)
node49 = TreeNode(49)
node48 = TreeNode(48, node12, node49)
node1 = TreeNode(1,node0,node48)

s = Solution()
print(s.minDiffInBST(node1))

