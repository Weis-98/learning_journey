# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        F1
        :param lists:
        :return:
        '''
        k = len(lists)
        head = ListNode()
        ans = head

        def calcu():
            minest = 10 ** 4
            mini = -1
            for i in range(k):
                if not lists[i]:
                    continue
                if lists[i].val <= minest:
                    mini = i
                    minest = lists[i].val
            return mini

        i = calcu()
        while i != -1:
            ans.next = lists[i]
            lists[i] = lists[i].next
            ans = ans.next

            i = calcu()

        return head.next


    def merge2list(self, list1, list2):
        head = ListNode()
        ans = head

        while list1 and list2:
            if list1.val <= list2.val:
                ans.next = list1
                list1 = list1.next
            else:
                ans.next = list2
                list2 = list2.next
            ans = ans.next
        while list1:
            ans.next = list1
            list1 = list1.next
            ans = ans.next
        while list2:
            ans.next = list2
            list2 = list2.next
            ans = ans.next

        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        F2
        :param lists:
        :return:
        '''
        k = len(lists)
        temp1 = lists
        while k > 1:
            temp = []
            for i in range(0, k, 2):
                if i + 1 < k:
                    temp.append(self.merge2list(temp1[i], temp1[i + 1]))
                else:
                    temp.append(temp1[i])
            temp1 = temp
            k = len(temp1)
        return temp[0]



