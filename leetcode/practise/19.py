# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        vir = ListNode(val=0, next=head)
        cnt = 0
        first = vir
        second = vir
        while cnt < n:
            second = second.next
            cnt += 1

        while second.next:
            first = first.next
            second = second.next

        first.next = first.next.next
        return vir.next

sec = ListNode(2, )
head = ListNode(1,sec)
s = Solution()
s.removeNthFromEnd(head, 2)