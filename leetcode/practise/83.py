# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        virtue = ListNode(0, head)
        if not head:
            return head
        cur = virtue
        while cur.next and cur.next.next:
            while cur.next.next and cur.next.val == cur.next.next.val:
                cur.next = cur.next.next
            cur = cur.next
        return virtue.next