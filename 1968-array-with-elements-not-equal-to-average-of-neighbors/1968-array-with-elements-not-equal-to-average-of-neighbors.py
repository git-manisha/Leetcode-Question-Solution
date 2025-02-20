class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i=1
        while(i<len(nums)-1):
            if((nums[i-1]+nums[i+1]) == nums[i]*2):
                nums[i],nums[i+1] = nums[i+1],nums[i]
            i +=1
        
        j = len(nums)-2
        while(j>0):
            if((nums[j+1]+nums[j-1]) == nums[j]*2):
                nums[j],nums[j+1] = nums[j+1],nums[j]
            j -=1
        
        return nums
        
