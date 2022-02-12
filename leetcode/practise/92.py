
"""给你单链表的头指针 head 和两个整数left 和 right ，其中left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        cur = head
        if cur.next == None or left == right:
            return head
        node0 = ListNode(next=head)
        before = node0
        for _ in range(left - 1):
            before = before.next

        cur = before.next
        L = cur
        for _ in range(right - left):
            after = cur.next
            temp = after.next
            after.next = cur
            cur = after
            after = temp
        before.next = cur
        L.next = after
        return node0.next
