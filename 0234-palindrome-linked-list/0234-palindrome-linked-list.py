# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseLinkedlist(self,head):
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

    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if(head==None or head.next==None):
            return True
        slow = head
        fast = head
        prev = None
        while(fast!=None and fast.next!=None):
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        last = self.reverseLinkedlist(slow)
        curr = head
        while(curr!=None and last!=None):
            if(curr.val != last.val):
                return False
            curr = curr.next
            last = last.next
        
        return True



        