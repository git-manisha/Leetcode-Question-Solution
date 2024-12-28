class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i =1
        while(i<len(nums) and nums[i-1]==nums[i]):
            i +=1
        
        if(i<len(nums) and nums[i-1]<nums[i]):
            while(i<len(nums)):
                if(nums[i-1]<=nums[i]):
                    pass
                else:
                    return False
                i +=1
        else:
            while(i<len(nums)):
                if(nums[i-1]>=nums[i]):
                    pass
                else:
                    return False
                i +=1

        return True
        