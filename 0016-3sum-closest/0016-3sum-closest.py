class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        i =0
        result = 0
        minimum = 1000
        while(i<len(nums)):
            j = i+1
            k = len(nums)-1
            while(j<k):
                total = nums[i]+nums[j]+nums[k]
                diff = abs(total - target)
                if(diff < minimum):
                    result = total
                    minimum = diff
                if(total < target):
                    j +=1
                else:
                    k -=1
            i +=1
        
        return result