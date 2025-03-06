class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for ch in s:
            if(len(stack)==0 or ch=='(' or ch=='{' or ch=='['):
                stack.append(ch)
                continue
            if(ch == ')'):
                if(stack[len(stack)-1] =='('):
                    stack.pop()
                else:
                    return False
            if(ch == '}'):
                if(stack[len(stack)-1] =='{'):
                    stack.pop()
                else:
                    return False
            if(ch == ']'):
                if(stack[len(stack)-1] =='['):
                    stack.pop()
                else:
                    return False

        if(stack):
            return False
        return True

