class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if(n==1):
            return [0,1]
        
        prev = self.grayCode(n-1)

        ans = prev

        for i in reversed(prev):
            ans.append(i+pow(2,n-1))
        
        return ans
        