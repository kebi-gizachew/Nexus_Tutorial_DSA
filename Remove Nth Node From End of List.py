# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        temp=ListNode(0,head)
        fast=slow=temp
        k=n
        while k>0:
            fast=fast.next
            k-=1
        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return temp.next
