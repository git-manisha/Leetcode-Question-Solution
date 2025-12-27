# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if(head == None):
            return head
        left = head
        right  = head.next
        
        while(right != None):
            if(left.val == right.val):
                left.next = right.next
                right = right.next
            else:
                left = right
                right = right.next
        return head
        