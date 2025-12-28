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
        slow = head
        fast = head
        p = None
        q = None

        while(fast != None and fast.next != None):
            p = q
            q = slow
            slow = slow.next
            fast = fast.next.next
            q.next = p
        
        if(fast != None):
            slow = slow.next
        
        while(q != None and slow != None):
            if(q.val != slow.val):
                return False
            q = q.next
            slow = slow.next
        
        return True