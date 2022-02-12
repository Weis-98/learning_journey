class Solution:
    def isValid(self, s: str) -> bool:
        def match(left, right):
            if left == '(' and right == ")":
                return True
            if left == '[' and right == "]":
                return True
            if left == '{' and right == "}":
                return True
            return False
        stack = []
        left = set(['(', "[", "{"])
        right = set([')', "]", "}"])
        for i in s:
            if i in left:
                stack.append(i)
            if i in right:
                if stack == []:
                    return False
                test = stack.pop()
                if match(test, i):
                    continue
                else:
                    return False
        return True and stack == []

