# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        global maxsum
        maxsum = -float('inf')

        def maxGain(root):
            global maxsum
            if not root:
                return 0
            left_gain = max(maxGain(root.left), 0)
            right_gain = max(maxGain(root.right), 0)
            princenewpath = root.val + left_gain + right_gain
            maxsum = max(maxsum, princenewpath)
            return root.val + max(left_gain, right_gain)

        maxGain(root)
        return maxsum

