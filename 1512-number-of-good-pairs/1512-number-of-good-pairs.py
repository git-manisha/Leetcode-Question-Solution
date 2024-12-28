class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}

        for i in nums:
            if(i not in hashmap):
                hashmap[i] = 1
            else:
                hashmap[i] +=1
        
        count =0
        for key,value in hashmap.items():
            if(value >1):
                count += (value*(value-1))/2
            
        return count