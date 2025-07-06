class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        itr = 0
        maximum = 0
        while(itr<len(rectangles)):
            rectangles[itr] = min(rectangles[itr])
            maximum = max(maximum,rectangles[itr])
            itr +=1
        
        count = 0
        for i in rectangles:
            if(i == maximum):
                count +=1

        return count
