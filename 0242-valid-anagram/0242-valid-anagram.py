class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s) != len(t)):
            return False
        my_list = [0]*26
        i=0
        l = len(s)
        while(i<l):
            it = ord(s[i])-ord('a')
            my_list[it] = my_list[it]+1
            i = i+1
        i=0
        length_t = len(t)
        while(i<length_t):
            it = ord(t[i])-ord('a')
            my_list[it] = my_list[it]-1
            i = i+1
        
        for i in range(26):
            if(my_list[i] != 0):
                return False

        return True
        
        