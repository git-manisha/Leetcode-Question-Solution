class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 1
        while(i<len(nums)):
            nums[i] = nums[i]+nums[i-1]
            i +=1
        
        return nums