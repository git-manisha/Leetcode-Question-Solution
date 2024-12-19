class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        if(len(strs)<2 or strs[0] ==""):
            return strs[0]
        str1 = strs[0]
        str2 = strs[len(strs)-1]
        ans = ""

        i =0
        while(i< len(strs[0])):
            if(str1[i] != str2[i]):
                return ans
            ans = ans + str1[i]
            i = i+1
        
        return ans
        