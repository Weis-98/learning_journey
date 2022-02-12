# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while True:
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        pos = head
        while pos:
            slow = pos.next
            fast = pos.next.next
            while fast:
                if fast.next is None or fast.next.next is None:
                    return None
                else:
                    if fast == pos or fast.next == pos:
                        return pos
                    if slow == fast:
                        break
                    fast = fast.next.next
                    slow = slow.next
            pos = pos.next

