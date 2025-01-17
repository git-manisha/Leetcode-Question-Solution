class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        presum = 0
        total = 0
        for itr in nums:
            total +=itr

        i=0
        sum1 =0
        s = len(nums)-1
        while(i<len(nums)):
            temp = ((nums[i]*i)-presum)+((total-presum-nums[i])-(nums[i]*(len(nums)-i-1)))
            presum +=nums[i]
            nums[i] = temp
            i +=1
        
        return nums