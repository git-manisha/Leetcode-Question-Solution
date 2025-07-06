class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        i =0
        j =0
        k = len(mat)-1
        total_sum = 0
        while(i<len(mat)):
            if(j==k):
                total_sum +=mat[i][j]
            else:
                total_sum += mat[i][j]+mat[i][k]
            i+=1
            j+=1
            k-=1
        
        return total_sum