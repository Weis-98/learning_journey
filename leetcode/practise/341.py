# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list = nestedList
        self.make_list()
        self.count = 0
        self.len = len(self.list)

    def make_list(self):
        while self.has_list():
            for i in range(len(self.list)):
                if not self.list[i].isInteger():
                    self.list = self.list[:i] + self.list[i].getList() + self.list[i+1:]
                    break

    def has_list(self):
        for i in self.list:
            if not i.isInteger():
                return True
        return False

    def next(self) -> int:
        num = self.list[self.count]
        self.count += 1
        return num

    def hasNext(self) -> bool:
        return self.count < self.len
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())