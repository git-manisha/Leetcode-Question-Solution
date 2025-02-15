class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        t =1
        while(i>=0):
            if(nums[i]==0):
                j=i
                while(j<len(nums)-t):
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    j +=1
                t +=1
            i = i-1
        
        return nums