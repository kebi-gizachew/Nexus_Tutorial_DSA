# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        p=None
        while slow:
            y=slow.next
            slow.next=p
            p=slow
            slow=y
        t=head
        while p:
            if p.val!=t.val:
                return False
            p=p.next
            t=t.next
        return True
