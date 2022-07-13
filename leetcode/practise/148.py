from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:

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


class Solution2:

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

        dum = ListNode(next=head)
        node = head

        len_list = 0

        while node:
            len_list += 1
            node = node.next

        sub_len = 1

        while sub_len < len_list:
            ahead = dum
            curr = dum.next
            while curr:
                head1 = curr
                for i in range(sub_len - 1):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                head2 = curr.next
                curr.next = None
                curr = head2

                for i in range(sub_len - 1):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break

                if curr:
                    tmp = curr.next
                    curr.next = None
                    curr = tmp

                ahead.next = merge(head1, head2)

                while ahead.next:
                    ahead = ahead.next

            sub_len *= 2

        return dum.next
