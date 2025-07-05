class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        str1 = ""
        str2 = ""

        for s in word1:
            str1 +=s
        for ch in word2:
            str2 +=ch
        
        if(str1 == str2):
            return True
        return False
        