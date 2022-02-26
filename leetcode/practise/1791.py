class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        testA, testB = edges[0]
        if testA in edges[1]:
            return testA
        if testB in edges[1]:
            return testB

