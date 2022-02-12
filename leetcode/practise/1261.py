class FindElements:

    def __init__(self, root: TreeNode):
        self.nums = {0}
        root.val = 0
        stack = [root]
        while stack:
            item = stack.pop()
            self.nums.add(item.val)
            if item.left:
                item.left.val = 2*item.val + 1
                stack.append(item.left)
            if item.right:
                item.right.val = 2*item.val + 2
                stack.append(item.right)
        self.root = root


    def find(self, target: int) -> bool:
        return target in self.nums