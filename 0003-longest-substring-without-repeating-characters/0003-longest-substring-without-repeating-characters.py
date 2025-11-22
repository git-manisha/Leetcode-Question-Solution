class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        right = 0
        left = 0
        hashmap = {}
        max_length = 0

        while(left<len(s)):
            if(s[left] in hashmap):
                while(s[right] != s[left]):
                    del hashmap[s[right]]
                    right +=1
                right +=1
                max_length = max(max_length,(left-right+1))
            else:
                hashmap[s[left]] = 1
                max_length = max(max_length,(left-right+1))
            left +=1
        
        #max_length = max(max_length,(left-right+1))

        return max_length