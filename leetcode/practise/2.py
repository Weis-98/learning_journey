# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        here = head

        up = 0
        while l1 and l2:
            here.next = ListNode(val=(l1.val + l2.val + up) % 10)
            up = (l1.val + l2.val + up) // 10
            l1 = l1.next
            l2 = l2.next
            here = here.next

        while l1:
            here.next = ListNode(val=(l1.val + up) % 10)
            up = (l1.val + up) // 10
            l1 = l1.next
            here = here.next
        while l2:
            here.next = ListNode(val=(l2.val + up) % 10)
            up = (l2.val + up) // 10
            l2 = l2.next
            here = here.next

        if up:
            here.next = ListNode(val=up)

        return head.next

