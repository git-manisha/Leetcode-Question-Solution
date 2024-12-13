class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        i =0;
        while(i<size):
            nums.append(nums[i])
            i = i+1
        
        return nums
        