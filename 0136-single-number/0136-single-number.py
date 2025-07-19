class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==1):
            return nums[0]
        
        ans = 0
        for n in nums:
            ans = ans^n
        
        return ans
        