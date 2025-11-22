class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = ""
        hashmap = {}
        max_length = 0
        if(len(s)==1):
            return 1
        first = 0
        last = 0
        while(last < len(s)):
            if(s[last] in hashmap):
                max_length = max(max_length,len(substring))
                while(s[first] != s[last]):
                    del hashmap[s[first]]
                    substring = substring[1:]
                    first +=1
                substring = substring[1:]
                first +=1
                substring +=s[last]
            else:
                substring +=s[last]
                hashmap[s[last]] = 1
            last +=1
        max_length = max(max_length,len(substring))
        return max_length
            
