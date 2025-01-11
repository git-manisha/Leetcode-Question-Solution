class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        unique = set()
        for i in s:
            unique.add(i)
        
        for ch in unique:
            i=0
            j =len(s)-1
            while(s[i] != ch):
                i +=1
            while(s[j] != ch):
                j -=1
            temp = set()
            i +=1
            while(i<j):
                temp.add(s[i])
                i+=1
            ans +=len(temp)
        
        return ans
        