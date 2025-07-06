class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        hashmap = {}
        i =0
        while(i<len(rectangles)):
            val = min(rectangles[i])
            if(val not in hashmap):
                hashmap[val] = 1
            else:
                hashmap[val] +=1
            i +=1
        
        maximum =0
        result = 0
        for key ,value in hashmap.items():
            if(key>maximum):
                maximum = key
                result = value
        
        return result