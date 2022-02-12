class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        queue = deque()
        queue.append(root)
        res = ''
        while queue:
            node = queue.popleft()  # collections 库中的queue 没有pop(0)操作，这是 list 的操作
            if node:  # 出列的节点，带出子节点入列
                res = res + str(node.val) + ','
                queue.append(node.left)  # 不管是不是 null 节点都入列
                queue.append(node.right)
            else:
                res = res + 'X,'
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')  # 序列化字符串转成 list 数组
        root = TreeNode(data.pop(0))  # 首项是根节点值，为其创建节点
        queue = [root]  # 初始放入 root，待会出列考察
        while queue:
            node = queue.pop(0)  # 父节点出列考察
            if data:
                val = data.pop(0)  # pop 出左子节点
                if val != 'X':  # 左子节点是有效值
                    node.left = TreeNode(val)  # 成为当前出列节点的左子节点
                    queue.append(node.left)  # 它是未来的父节点，入列等待考察
            if data:
                val = data.pop(0)  # pop 出右子节点
                if val != 'X':  # 右子节点是有效值
                    node.right = TreeNode(val)
                    queue.append(node.right)
        return root

