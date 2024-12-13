class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dit = dict()
        for i in s:
            if i not in dit:
                dit[i] = 1
            else:
                dit[i] = dit[i]+1
        
        for i in t:
            if i in dit:
                dit[i] = dit[i]-1
            else:
                return False
        
        for i in dit:
            if dit[i]>0 or dit[i]<0:
                return False
        
        return True

        