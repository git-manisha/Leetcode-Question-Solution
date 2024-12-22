class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s) != len(t)):
            return False
        res = {}
        res1 = {}
        i=0
        while(i<len(s)):
            if(s[i] not in res):
                res[s[i]] = t[i]
            else:
                if(res[s[i]] != t[i]):
                    return False
            i +=1
        i=0
        while(i<len(s)):
            if(t[i] not in res1):
                res1[t[i]] = s[i]
            else:
                if(res1[t[i]] != s[i]):
                    return False
            i +=1
        
        return True

        
