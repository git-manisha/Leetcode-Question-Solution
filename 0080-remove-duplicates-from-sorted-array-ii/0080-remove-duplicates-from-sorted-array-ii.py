class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=0
        while(j<len(nums)):
            if(nums[i]==nums[j] and (j-i+1)>2):
                nums.remove(nums[j])
            elif(nums[i]!=nums[j]):
                i +=1
                j +=1
            else:
                j +=1
        
        k = 0
        for i in nums:
            k +=1
        
        return k