class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        stops = [0]*1001
        i = 0
        while(i<len(trips)):
            stops[trips[i][1]] +=trips[i][0]
            stops[trips[i][2]] -=trips[i][0]
            i +=1
        
        i =1
        if(stops[0]>capacity):
            return False
        while(i<len(stops)):
            stops[i] = stops[i]+stops[i-1]
            if(stops[i]>capacity):
                return False
            i +=1
        
        return True
            