class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0):
            return 0
        nums.sort()
        count = 1
        largest =1
        i=1
        while(i<len(nums)):
            if(nums[i-1]+1 == nums[i]):
                count +=1
            else:
                largest = max(count,largest)
                count =1
            i +=1
        
        largest = max(count,largest)
        
        return largest
        
        