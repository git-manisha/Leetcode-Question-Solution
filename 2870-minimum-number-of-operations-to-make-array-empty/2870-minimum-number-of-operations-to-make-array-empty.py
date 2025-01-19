class Solution(object):
    def minOperations(self, nums):
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
        
        count = 0

        for key,value in hashmap.items():
            if(value<2):
                return -1
            elif(value%3 == 0):
                count +=value/3
            elif((value-1)%3==0):
                count = count+((value-4)/3)+2
            elif((value-2)%3 == 0):
                count = count+(value-2)/3 +1
            elif(value%2==0):
                count +=value/2
        
        return count