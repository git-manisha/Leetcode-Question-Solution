class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_str = ""
        i=0

        while(i<len(s)):

            if(s[i].isalpha()):
                if(s[i].isupper()):
                    new_str +=s[i].lower()
                else:
                    new_str +=s[i]
            elif(s[i].isnumeric()):
                new_str +=s[i]
            i+=1
        
        i=0
        j= len(new_str)-1
        while(i<j):
            if(new_str[i] != new_str[j]):
                return False
            i +=1
            j -=1
        
        return True
        