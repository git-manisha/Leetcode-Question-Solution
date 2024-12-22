class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map1 = {}

        size =0
        if(len(nums)%2 ==0):
            size = len(nums)/2
        else:
            size = len(nums)/2+1

        for i in nums:
            if i not in map1:
                map1[i] = 1
            else:
                map1[i] = map1[i]+1
        
        res = 0
        for key,value in map1.items():
            if(value >=size):
                res = key
        
        return res

        