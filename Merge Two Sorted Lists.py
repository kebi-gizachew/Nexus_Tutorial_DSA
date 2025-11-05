# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        t1,t2=list1,list2
        dummy=ListNode(0)
        t=dummy
        while t1 and t2:
            if t1.val<t2.val:
                t.next=t1
                t=t.next
                t1=t1.next
            else:
                t.next=t2
                t=t.next
                t2=t2.next
        if t1:
            t.next=t1
        if t2:
            t.next=t2
        return dummy.next
