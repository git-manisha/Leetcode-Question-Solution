class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        str1 = ""
        result = ""
        itr = 0
        while(itr<len(s)):
            if(s[itr]==" " and k!=0):
                result += str1 +" "
                str1 = ""
                k -=1
            elif(k==0):
                return result[:-1]
            else:
                str1 +=s[itr]
            itr +=1
        
        return result+str1
            