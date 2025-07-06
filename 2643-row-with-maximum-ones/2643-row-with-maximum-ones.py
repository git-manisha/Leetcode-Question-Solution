class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        result = [0]*2
        count = 0
        maxi = 0
        first = 0
        while(first<len(mat)):
            second = 0
            while(second<len(mat[first])):
                count +=mat[first][second]
                second +=1
            if(count>maxi):
                maxi = count
                result[0]=first
                result[1]=count
            count = 0
            first +=1
        
        return result