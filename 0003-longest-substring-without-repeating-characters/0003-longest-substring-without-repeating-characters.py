class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        queue = []
        i = 0
        result = 0
        substr = ""
        while(i<len(s)):
            if(s[i] in queue):
                while(len(queue)!=0 and queue[0]!=s[i]):
                    del queue[0]
                del queue[0]
                queue.append(s[i])
            else:
                queue.append(s[i])
            if(len(queue)>result):
                result = len(queue)
            i +=1 
        return result

                   