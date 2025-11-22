class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        zeros = 0
        count = 0
        max_count = 0
        left = 0
        right = 0

        while(right <len(nums)):
            if(nums[right]==0):
                zeros +=1
            while(left<=right and zeros==(k+1)):
                if(nums[left]==0):
                    zeros -=1
                left +=1
            max_count = max(max_count,(right-left+1))
            right+=1
        
        return max_count
        