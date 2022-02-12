# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        virtue = ListNode(-1, head)
        if not head:
            return head
        cur = virtue
        while cur.next and cur.next.next:
            if cur.next.val != cur.next.next.val:
                cur = cur.next
            else:
                num = cur.next.val
                while cur.next and cur.next.val == num:
                    cur.next = cur.next.next
        return virtue.next