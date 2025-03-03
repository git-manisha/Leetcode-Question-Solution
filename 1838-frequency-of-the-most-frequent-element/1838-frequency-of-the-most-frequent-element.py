def BinarySearch(target,nums,k,l1):
    l=0
    r = target
    result =0
    while(l<=r):
        mid = l+(r-l)/2
        count = (target-mid+1)
        window_sum = count * nums[target]
        presum = l1[target]-l1[mid]+nums[mid]
        rem = window_sum-presum
        if(rem>k):
            l = mid +1
        else:
            result = mid
            r = mid-1
    
    return target-result+1

        

class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l1 = []
        i =0
        presum = 0
        while(i<len(nums)):
            presum +=nums[i]
            l1.append(presum)
            i +=1

        i = 0
        res = 0
        while(i<len(nums)):
            val = BinarySearch(i,nums,k,l1)
            res = max(res,val)
            i +=1

        return res
