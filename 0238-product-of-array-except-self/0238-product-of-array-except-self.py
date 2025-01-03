class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product=1
        res = [0]*len(nums)
        count =0
        for i in nums:
            if(i==0):
                count +=1
            else:
                product = product*i
            if(count ==2):
                return res
        
        i=0
        while(i<len(nums)):
            if(nums[i] == 0):
                res[i] = product
                return res
            else:
                nums[i] = product/nums[i]
            i +=1
        
        return nums
            
        

        
        