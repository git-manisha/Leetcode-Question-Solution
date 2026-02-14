class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if(k==1):
            return 0
        
        parent = self.kthGrammar(n-1,int((k+1)/2))

        if(parent==0):
            if(k%2==1):
                return 0
            else:
                return 1
        else:
            if(k%2==1):
                return 1
            else:
                return 0
        