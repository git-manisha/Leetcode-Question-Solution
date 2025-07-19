class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        hashmap = {}
        cost1 = 0
        cost2 = 0
        i = 0
        while(i<len(position)):
            if(position[i]%2 != 0):
                cost1 +=1
            else:
                cost2 +=1
            i +=1


        return cost1 if cost1<cost2 else cost2


        