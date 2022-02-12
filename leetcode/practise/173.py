# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# F1
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.num = -1
        self.virtue = TreeNode(self.num, root)
        self.list = [self.virtue]
        self.cur = self.virtue

    def next(self) -> int:
        while self.list:
            if self.cur.left and self.cur.left.val > self.num:
                self.list.append(self.cur)
                self.cur = self.cur.left
                continue
            elif self.cur.val > self.num:
                self.num = self.cur.val
                return self.num
            elif self.cur.right and self.cur.right.val > self.num:
                self.list.append(self.cur)
                self.cur = self.cur.right
                continue
            self.cur = self.list.pop()

    def hasNext(self) -> bool:
        while self.list:
            if self.cur.left and self.cur.left.val > self.num:
                self.list.append(self.cur)
                self.cur = self.cur.left
                continue
            elif self.cur.val > self.num:
                return True
            elif self.cur.right and self.cur.right.val > self.num:
                self.list.append(self.cur)
                self.cur = self.cur.right
                continue
            self.cur = self.list.pop()
        return False

# F2
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.list = []
        cur = root
        while cur:
            self.list.append(cur)
            cur = cur.left

    def next(self) -> int:
        tmp = self.list.pop()
        if tmp.right:
            cur = tmp.right
            while cur:
                self.list.append(cur)
                cur = cur.right
        return tmp.val

    def hasNext(self) -> bool:
        if self.list:
            return True
        return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


# test
node3 = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15, node9, node20)
root = TreeNode(7, node3, node15)

obj = BSTIterator(root)
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.hasNext())

