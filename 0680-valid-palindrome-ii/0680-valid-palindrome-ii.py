def isPalindrom(s,f,l):
    while(f<l):
        if(s[f]!=s[l]):
            return False
        f +=1
        l -=1
    return True
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count =1
        i=0
        j=len(s)-1
        while(i<j):
            if(s[i]!=s[j]):
                return isPalindrom(s,i+1,j) or isPalindrom(s,i,j-1)
            i +=1
            j -=1 
        
        return True


        