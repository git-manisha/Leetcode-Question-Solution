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
        p = head
        q = None
        r = None
        while(p != None):
            r = q
            q = p
            p = p.next
            q.next = r
        head = q
        return head
        