class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for i in words:
            str1 = i
            str1 = "".join(reversed(str1))
            if(str1 == i):
                return i
        
        return ""
        