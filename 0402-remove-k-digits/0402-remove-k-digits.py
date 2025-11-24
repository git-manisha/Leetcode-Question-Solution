class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        i=0
        if(len(num)<=k):
            return "0"
        while(i<len(num) and k!=0):
            digit = num[i]
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
            i+=1
        
        while(k != 0):
            stack.pop()
            k -=1
        while(i<len(num)):
            stack.append(num[i])
            i +=1
        
        
        result = ""
        for i in stack:
            result +=str(i)

        while(result[0]=="0" and len(result)!=1):
            result = result[1:]
        return result
            
