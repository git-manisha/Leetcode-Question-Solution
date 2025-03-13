class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for star in s:
            if star == '*':
                stack.pop()
            else:
                stack.append(star)
        
        result = ""
        i = len(stack)-1
        while(i>=0):
            result = stack.pop()+result
            i -=1
        return result

        