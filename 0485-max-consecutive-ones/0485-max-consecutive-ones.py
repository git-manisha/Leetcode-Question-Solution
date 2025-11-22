class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_count = 0
        i =0
        while(i<len(nums)):
            if(nums[i] == 0):
                count = 0
            else:
                count +=nums[i]
            max_count = max(max_count,count)
            i +=1
        
        return max_count
        