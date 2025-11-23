class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        i =0
        while(i<len(s)):
            if(len(stack)!=0 and s[i] == stack[len(stack)-1]):
                stack.pop()
            else:
                stack.append(s[i])
            i +=1
        
        result = ""
        i = 0
        while(i<len(stack)):
            result +=stack[i]
            i+=1
        
        return result


        