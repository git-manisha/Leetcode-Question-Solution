class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []

        i = 0
        while(i<len(pushed)):
            stack.append(pushed[i])
            while(len(stack)!=0 and (stack[len(stack)-1] == popped[0])):
                stack.pop()
                del popped[0]
            i +=1
        
        if(len(stack)==0):
            return True
        return False
            

        