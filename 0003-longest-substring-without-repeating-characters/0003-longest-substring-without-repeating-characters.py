class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {}
        i = 0
        j = 0
        result = 0
        substr = ""
        while(i<len(s)):
            if(s[i] in hashmap):
                hashmap[s[i]] = i
                while(len(substr)!=0 and substr[j] != s[i]):
                    substr = substr[1:]
                if(len(substr) ==0):
                    substr = ""
                else:
                    substr = substr[1:]
                substr +=s[i]
            else:
                substr +=s[i]
                hashmap[s[i]] = i
            if(len(substr)>result):
                result = len(substr)
            i +=1
        
        return result
                   