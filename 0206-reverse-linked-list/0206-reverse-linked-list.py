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
        curr = head
        p = None
        q = None
        
        while(curr != None):
            p = q
            q = curr
            curr = curr.next
            q.next = p
        
        head = q
        return head
        