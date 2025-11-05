# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow,fast=head,head
        sy=fy=0
        while fast!=slow:
            if sy>1 or fy>1:
                break
            if slow:
                slow=slow.next
            else:
                slow=fast
                sy+=1
            if fast:
                fast=fast.next
            else:
                fy+=1
                fast=slow
        if fast==slow:
            return slow
        return -1
