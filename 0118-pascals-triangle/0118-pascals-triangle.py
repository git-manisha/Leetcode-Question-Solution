class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(numRows):
            j =0
            temp = []
            while(j<i):
                if(j ==0):
                    temp.append(1)
                else:
                    temp.append(ans[i-1][j]+ans[i-1][j-1])
                j = j+1
            temp.append(1)
            ans.append(temp)
        
        return ans

            
        