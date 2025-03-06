class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack =[]

        for ch in s:
            if(ch == '('):
                stack.append(')')
            elif(ch == '{'):
                stack.append('}')
            elif(ch == '['):
                stack.append(']')
            elif(len(stack)==0 or stack[len(stack)-1] != ch):
                return False
            else:
                stack.pop()
            
        if(stack):
            return False
        return True

        