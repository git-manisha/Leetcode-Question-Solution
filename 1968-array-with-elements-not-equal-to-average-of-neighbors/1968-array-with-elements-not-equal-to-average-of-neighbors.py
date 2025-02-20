class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        l1 = [0]*len(nums)
        i =0
        j=0
        while(i<len(nums)):
            l1[i] = nums[j]
            i +=2
            j +=1
        i =1
        while(i<len(nums)):
            l1[i] = nums[j]
            i +=2
            j +=1
        
        return l1
        
        

        