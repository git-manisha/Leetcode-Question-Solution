class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        str_list = []
        j=0
        substr = ''
        for ch in s:
            if(ch == ' '):
                str_list.append(substr)
                substr = ''
            else:
                substr +=ch
        str_list.append(substr)
        
        if(len(pattern) != len(str_list)):
            return False
        
        hashmap = {}
        i=0
        while(i<len(pattern)):
            if(pattern[i] not in hashmap):
                hashmap[pattern[i]] = str_list[i]
            else:
                if(hashmap[pattern[i]] != str_list[i]):
                    return False
            i +=1
        hashmap.clear()
        i=0
        while(i<len(str_list)):
            if(str_list[i] not in hashmap):
                hashmap[str_list[i]] = pattern[i]
            else:
                if(hashmap[str_list[i]] != pattern[i]):
                    return False
            i +=1

        return True

        