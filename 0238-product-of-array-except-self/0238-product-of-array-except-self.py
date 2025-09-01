class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zeroCount = 0
        multiple = 1
        for i in nums:
            if i == 0:
                zeroCount +=1
            else:
                multiple *=i
        
        newArr = [0]*len(nums)
        if zeroCount==0:
            i = 0
            while(i<len(nums)):
                newArr[i] = multiple//nums[i]
                i +=1
        elif zeroCount==1:
            i = 0
            while(i<len(nums)):
                if nums[i]==0:
                    newArr[i] = multiple
                i +=1
        
        return newArr

