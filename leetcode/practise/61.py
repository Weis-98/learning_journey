# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        cur = head
        len_l = 1
        while cur.next:
            cur = cur.next
            len_l += 1
        cur.next = head

        cur2 = head
        for i in range(len_l - 1 - k%len_l):
            cur2 = cur2.next
        head = cur2.next
        cur2.next = None
        return head