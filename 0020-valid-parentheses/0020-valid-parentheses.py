class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        i=0
        while(i<len(s)):
            if(stack):
                if((s[i] == ')' and stack[len(stack)-1]=='(') or (s[i] == '}' and stack[len(stack)-1]=='{') or (s[i] == ']' and stack[len(stack)-1]=='[')):
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])

            i +=1
        
        if(stack):
            return False
        return True

