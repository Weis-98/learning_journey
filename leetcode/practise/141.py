# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            slow = slow.next
            fast = fast.next
            if fast is None or fast.next is None:
                return False
            else:
                fast = fast.next
        return True

