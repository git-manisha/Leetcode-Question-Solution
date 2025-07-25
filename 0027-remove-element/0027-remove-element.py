class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = len(nums)

        first = 0
        last = len(nums)-1

        while(first<=last):
            if(nums[first]==val):
                while(first<last and nums[last]==val):
                    del nums[last]
                    last -=1
                nums[first], nums[last] = nums[last], nums[first]
                del nums[last]
                last -=1
            first +=1
        
        return len(nums)
            
            
