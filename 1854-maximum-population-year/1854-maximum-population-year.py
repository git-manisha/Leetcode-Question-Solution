class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        prefix = [0]*2056
        i =0
        while(i<len(logs)):
            prefix[logs[i][0]] +=1
            prefix[logs[i][1]] -=1
            i +=1
        
        i =1950
        while(i<len(prefix)):
            prefix[i] = prefix[i]+prefix[i-1]
            i +=1
        
        maxYear = 1950
        i = 1950
        while(i<len(prefix)):
            if(prefix[i]>prefix[maxYear]):
                maxYear = i
            i +=1
        
        return maxYear

        