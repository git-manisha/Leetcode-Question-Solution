class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s)-1
        while(s[i] == " "):
            i = i-1
        
        size = 0
        while(s[i] != " " and i>=0):
            size = size+1
            i = i-1
        
        return size
        