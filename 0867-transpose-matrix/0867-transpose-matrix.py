class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        list1 = []
        col = 0
        while(col<len(matrix[0])):
            row = 0
            temp = []
            while(row<len(matrix)):
                temp.append(matrix[row][col])
                row +=1
            list1.append(temp)
            col +=1

        return list1
