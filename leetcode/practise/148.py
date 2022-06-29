from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge(head1: ListNode, head2: ListNode):
            virtual = ListNode()
            node = virtual

            while head1 is not None and head2 is not None:
                if head1.val < head2.val:
                    node.next = head1
                    head1 = head1.next
                else:
                    node.next = head2
                    head2 = head2.next
                node = node.next

            if head1 is not None:
                node.next = head1
            elif head2 is not None:
                node.next = head2

            return virtual.next

        def sortPart(head: ListNode, tail: ListNode):
            if head is None:
                return head
            if head == tail:
                head = None
                return head

            fast = head
            slow = head
            while fast is not tail:
                fast = fast.next
                slow = slow.next
                if fast is not tail:
                    fast = fast.next

            h1 = sortPart(slow.next, tail)
            slow.next = None
            h2 = sortPart(head, slow)
            head = merge(h1, h2)
            return head

        return sortPart(head, None)