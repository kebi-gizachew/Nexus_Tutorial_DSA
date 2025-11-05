# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        o=ListNode(head.val)
        while head.next:
            head=head.next
            y=ListNode(head.val)
            y.next=o
            o=y
        return o
