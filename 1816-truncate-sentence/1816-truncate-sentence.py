class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        word_list = s.split()

        result = ""
        for i in word_list:
            if(k!=0):
                result += i +" "
            else:

                return result[:-1]
            k -=1
        
        return result[:-1]
        

        
        