class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if(len(needle)>len(haystack)):
            return -1
        j=0
        i=0
        sub_str = ""
        while(i<len(needle)-1):
            sub_str +=haystack[i]
            i +=1
        
        while(i<len(haystack)):
            sub_str += haystack[i]
            if(sub_str == needle):
                return j
            j +=1
            sub_str = sub_str[1:]
            i +=1
        
        return -1